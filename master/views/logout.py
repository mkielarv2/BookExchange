from django.contrib.auth import logout as authLogout
from django.shortcuts import resolve_url
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView


class Logout(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        authLogout(request)
        return Response({"status": "success"}, status=200)
