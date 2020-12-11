from django.http import JsonResponse
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated

from offers.models import Category, CategorySerializer, Localization, LocalizationSerializer, BookCondition, \
    BookConditionSerializer


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

