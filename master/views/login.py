from django.conf import settings
from django.contrib.auth import authenticate
from django.contrib.auth import login as authLogin
from django.shortcuts import resolve_url
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView


class Login(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        if request.user.is_authenticated:
            return Response({"status": "failure", "redirect": resolve_url(settings.LOGIN_REDIRECT_URL)}, status=422)

        payload = request.data

        email = payload["email"]
        password = payload["password"]

        user = authenticate(request, username=email, password=password)

        if user is None:
            responsePayload = {
                "status": "failure",
                "cause": "credentials",
                "desc": "Invalid user or password."
            }
            return Response(responsePayload, status=401)

        authLogin(request, user)

        responsePayload = {
            "status": "success",
            "redirect": resolve_url(settings.LOGIN_REDIRECT_URL)
        }
        return Response(responsePayload, status=200)
