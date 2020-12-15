import datetime

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

        if 'email' not in payload or 'password' not in payload:
            return Response({"status": "failure", "desc": "missing email or password field"}, status=400)
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
            "redirect": resolve_url(settings.LOGIN_REDIRECT_URL),
            "id": user.id
        }

        response = Response(responsePayload, status=200)

        expires = datetime.datetime.strftime(
            datetime.datetime.utcnow() + datetime.timedelta(seconds=365 * 24 * 60 * 60),
            "%a, %d-%b-%Y %H:%M:%S GMT",
        )
        response.set_cookie(
            'my_id',
            request.user.id,
            max_age=365 * 24 * 60 * 60,
            expires=expires,
            domain=settings.SESSION_COOKIE_DOMAIN,
            secure=settings.SESSION_COOKIE_SECURE or None,
        )

        return response
