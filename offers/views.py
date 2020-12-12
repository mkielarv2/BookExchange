import json

from django.http import JsonResponse, HttpResponseForbidden, HttpResponse
from django.utils import timezone
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated

from offers.models import Category, CategorySerializer, Localization, LocalizationSerializer, BookCondition, \
    BookConditionSerializer, Offers, OffersSerializer, OffersDeserializer, ImageURL


def get_all_objects(model, serializer):
    categories = model.objects.all()
    serializer = serializer(categories, many=True)
    return serializer.data


@api_view(['GET'])
def get_categories(request):
    """Get all category object"""
    return JsonResponse(get_all_objects(Category, CategorySerializer), safe=False)


@api_view(['GET'])
def get_localizations(request):
    """Get all category object"""
    return JsonResponse(get_all_objects(Localization, LocalizationSerializer), safe=False)


@api_view(['GET'])
def get_conditions(request):
    """Get all category object"""
    return JsonResponse(get_all_objects(BookCondition, BookConditionSerializer), safe=False)


@api_view(['DELETE'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def delete_offer(request, offer_id):
    """Delete offer"""
    offer = get_object_or_404(Offers, pk=offer_id)
    if offer.user != request.user:
        return HttpResponseForbidden()
    offer.is_deleted = True
    offer.save()
    return HttpResponse("{'status': 'success'}", status=200)


@api_view(['GET'])
def get_offer(request, offer_id):
    """Get details of offer"""
    offer = get_object_or_404(Offers, pk=offer_id)
    serializer = OffersSerializer(offer)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def get_user_offers(request, user_id):
    """Get offers of one user"""
    offers = Offers.objects.filter(is_deleted=False).filter(user__id=user_id)
    serializer = OffersSerializer(offers, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def get_offers(request):
    """Get offers"""
    filters = request.GET
    offers = Offers.objects.filter(is_deleted=False)
    if 'category' in filters:
        offers = offers.filter(category__id=filters['category'])
    if 'condition' in filters:
        offers = offers.filter(conditon__id=filters['condition'])
    if 'localization' in filters:
        offers = offers.filter(localization__id=filters['localization'])
    if 'author' in filters:
        offers = offers.filter(author__contains=filters['author'])
    if 'title' in filters:
        offers = offers.filter(title__contains=filters['title'])
    serializer = OffersSerializer(offers, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def create_offer(request):
    """Create offer"""
    deserializer = OffersDeserializer(data=json.loads(request.POST['payload']))
    if deserializer.is_valid():
        offer = deserializer.save(date=timezone.now(), user=request.user)
        for file in request.FILES:
            url = ImageURL()
            url.image = file
            url.offer_id = offer.id
            url.save()
        return HttpResponse('{"status": "success"}', status=200)
    return HttpResponse('{"status": "failure"}', status=400)
