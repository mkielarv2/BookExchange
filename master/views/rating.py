import json

from django.http import JsonResponse
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated

from master.models import RatingDeserializer, Rating


@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def rate(request):
    payload = request.data.get('payload')
    if not payload:
        return JsonResponse({'status': 'failure', 'desc': 'missing payload argument'}, status=400)
    serializer = RatingDeserializer(data=json.loads(payload))
    if serializer.is_valid():
        serializer.save(user=request.user)
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'failure', 'desc': serializer.errors}, status=422)


@api_view(['DELETE'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def delete_rate(request, user_id):
    rating = Rating.objects.filter(rated_user__id=user_id).filter(user=request.user).first()
    if not rating:
        return JsonResponse({'status': 'failure', 'desc': 'rating not found'}, status=404)
    rating.delete()
    return JsonResponse({'status': 'success'})
