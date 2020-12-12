from django.http import HttpResponse
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated

from master.models import UserDeserializer


@api_view(['PATCH'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def edit_user(request):
    """Edit your account"""
    serializer = UserDeserializer(request.data['payload'], instance=request.user)
    if serializer.is_valid():
        serializer.save()
        return HttpResponse('{"status": "success"}', status=200)
    return HttpResponse('{"status": "failure"}', status=400)
