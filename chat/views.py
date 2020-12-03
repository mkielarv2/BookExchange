from django.contrib.auth.models import User
from django.db.models import Q
from django.http import JsonResponse, HttpResponseForbidden, HttpResponseBadRequest
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from chat.models import MessagesSerializer, Messages
from master.models import UserSerializer
from offers.models import Offers


class MessagesView(APIView):
    """View for sending and receiving messages"""
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer = MessagesSerializer

    def get(self, request, offer_id, sender_id=None):
        """Get messages from chat"""
        offer = Offers.objects.get(pk=offer_id)
        if sender_id is None:
            if offer.user == request.user:
                return HttpResponseBadRequest()
            sender_id = request.user.id
        messages = Messages.objects.filter(offer__id=offer_id).order_by('sending_time')  # Get all messages to offer
        messages = messages.filter(Q(sender__id=offer.user.id) | Q(sender__id=sender_id))  # Filter messages only from and to sender
        serializer = self.serializer(messages, many=True)
        return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def get_chat_view(request, offer_id):
    """View for author of the offer to get users that started"""
    offer = Offers.objects.get(pk=offer_id)
    if offer.user != request.user:
        return HttpResponseForbidden()
    user_ids = Messages.objects.values('sender__id').filter(offer=offer).filter(~Q(sender=request.user)).distinct()
    users = User.objects.filter(id__in=user_ids)
    serializer = UserSerializer(users, many=True)
    return JsonResponse(serializer.data, safe=False)
