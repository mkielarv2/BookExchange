import json

from django.contrib.auth.models import User
from django.db.models import Q
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponse
from django.utils.datetime_safe import datetime
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated

from chat.models import MessagesSerializer, Messages, MessagesDeserializer, Comment, CommentSerializer, \
    CommentDeserializer
from master.models import UserSerializer
from offers.models import Offers


@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def get_chat(request, offer_id):
    """Get chats for offer"""
    offer = Offers.objects.get(pk=offer_id)
    user_ids = Messages.objects.values('sender__id').filter(offer=offer).filter(~Q(sender=request.user)).distinct()
    users = User.objects.filter(id__in=user_ids)
    serializer = UserSerializer(users, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def send_message(request):
    """Send message"""
    deserializer = MessagesDeserializer(data=json.loads(request.POST['payload']))
    if not deserializer.is_valid():
        return HttpResponseBadRequest(json.dumps(deserializer.errors))
    message = deserializer.save(sender=request.user, sending_time=datetime.now())
    if message.sender != message.offer.user and message.recipient != message.offer.user:
        message.delete()
        return HttpResponseBadRequest('One of users must be creator of the offer!')
    return HttpResponse(status=200)


@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def get_messages(request, offer_id, user_id):
    """Get messages from chat"""
    user = request.user
    messages = Messages.objects.filter(offer__id=offer_id).order_by('sending_time')  # Get all messages to offer
    query = (Q(sender__id=user_id) & Q(recipient=user)) | (Q(recipient__id=user_id) & Q(sender=user))
    messages = messages.filter(query)  # Filter messages only from and to user
    serializer = MessagesSerializer(messages, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def get_comments(request, user_id):
    """Get comments about user"""
    comments = Comment.objects.filter(user__id=user_id)
    serializer = CommentSerializer(comments, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def add_comment(request):
    """Add comment about user"""
    deserializer = CommentDeserializer(data=json.loads(request.POST['payload']))
    if not deserializer.is_valid():
        return HttpResponseBadRequest(json.dumps(deserializer.errors))
    deserializer.save(author=request.user, adding_time=datetime.now())
    return HttpResponse(status=200)
