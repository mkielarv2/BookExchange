import json

from django.http import HttpResponse
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated

from master.models import RatingDeserializer, Rating


@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def rate(request):
    serializer = RatingDeserializer(data=json.loads(request.data['payload']))
    if serializer.is_valid():
        serializer.save(user=request.user)
        return HttpResponse('{"status": "success"}', status=200)
    print(serializer.errors)
    return HttpResponse('{"status": "failure"}', status=400)


@api_view(['DELETE'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def delete_rate(request, user_id):
    rating = Rating.objects.filter(rated_user__id=user_id).filter(user=request.user).first()
    if not rating:
        return HttpResponse('{"status": "failure"}', status=404)
    rating.delete()
    return HttpResponse('{"status": "success"}', status=200)
