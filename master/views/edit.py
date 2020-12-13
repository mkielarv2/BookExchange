import json

from django.http import JsonResponse
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated

from master.models import UserDeserializer


@api_view(['PATCH'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def edit_user(request):
    """Edit your account"""
    payload = request.data.get('payload')
    if not payload:
        return JsonResponse({'status': 'failure', 'desc': 'missing payload argument'}, status=400)
    serializer = UserDeserializer(data=json.loads(payload), instance=request.user)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'failure', 'desc': serializer.errors}, status=400)
