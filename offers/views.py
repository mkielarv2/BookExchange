import json

from django.db.models import Q
from django.http import JsonResponse
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
    """Get all localizations object"""
    return JsonResponse(get_all_objects(Localization, LocalizationSerializer), safe=False)


@api_view(['GET'])
def get_conditions(request):
    """Get all conditions object"""
    return JsonResponse(get_all_objects(BookCondition, BookConditionSerializer), safe=False)


@api_view(['DELETE'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def delete_offer(request, offer_id):
    """Delete offer"""
    offer = get_object_or_404(Offers, pk=offer_id)
    if offer.user != request.user:
        return JsonResponse({'status': 'failure', 'desc': 'access forbidden'}, status=403)
    offer.is_deleted = True
    offer.save()
    return JsonResponse({'status': 'success'})


@api_view(['GET'])
def get_offer(request, offer_id):
    """Get details of offer"""
    offer = get_object_or_404(Offers, pk=offer_id)
    serializer = OffersSerializer(offer)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def get_user_offers(request, user_id):
    """Get offers of one user"""
    offers = Offers.objects.filter(user__id=user_id)
    serializer = OffersSerializer(offers, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def get_offers(request):
    """Get offers"""
    filters = request.GET
    offers = Offers.objects.filter(is_deleted=False)
    if 'category' in filters and len(filters['category']) and filters['category'] != 'undefined':
        offers = offers.filter(category__id=filters['category'])
    if 'condition' in filters and len(filters['condition']) and filters['condition'] != 'undefined':
        offers = offers.filter(condition__id=filters['condition'])
    if 'localization' in filters and len(filters['localization']) and filters['localization'] != 'undefined':
        offers = offers.filter(location__id=filters['localization'])
    if 'author' in filters and len(filters['author']) and filters['author'] != 'undefined':
        offers = offers.filter(Q(author__icontains=filters['author']) | Q(title__icontains=filters['author']))
    if 'title' in filters and len(filters['title']) and filters['title'] != 'undefined':
        offers = offers.filter(Q(author__icontains=filters['title']) | Q(title__icontains=filters['title']))
    if 'sort' in filters and len(filters['sort']) > 1 and filters['sort'] != 'undefined':
        offers = offers.order_by(filters['sort'])
    serializer = OffersSerializer(offers, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def create_offer(request):
    """Create offer"""
    payload = request.POST.get('payload')
    if not payload:
        return JsonResponse({'status': 'failure', 'desc': 'missing payload argument'}, status=400)
    deserializer = OffersDeserializer(data=json.loads(payload))
    if deserializer.is_valid():
        offer = deserializer.save(date=timezone.now(), user=request.user)
        files = []
        for file_list in request.FILES:
            for file in request.FILES.getlist(file_list):
                files.append(file)
        if len(files) > 5:
            files = files[:5]
        for file in files:
            url = ImageURL(image=file, offer_id=offer)
            url.save()
        return JsonResponse({'status': 'success'}, status=201)
    return JsonResponse({'status': 'failure', 'desc': deserializer.errors}, status=422)


@api_view(['PATCH'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def edit_offer(request, offer_id):
    """Edit offer"""
    payload = request.data.get('payload')
    if not payload:
        return JsonResponse({'status': 'failure', 'desc': 'missing payload argument'}, status=400)
    offer = get_object_or_404(Offers, pk=offer_id)
    if offer.user != request.user:
        return JsonResponse({'status': 'failure', 'desc': 'access forbidden'}, status=403)
    serializer = OffersDeserializer(data=json.loads(payload), instance=offer)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'failure', 'desc': serializer.errors}, status=422)
