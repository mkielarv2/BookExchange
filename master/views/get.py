from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404

from master.models import UserSerializer


@api_view(['GET'])
def get_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    serializer = UserSerializer(user)
    return JsonResponse(serializer.data, safe=False)
