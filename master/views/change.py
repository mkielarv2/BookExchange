import json

from django.conf import settings
from django.contrib.auth import update_session_auth_hash, password_validation
from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.shortcuts import resolve_url
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView


class Change(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        payload = request.data["payload"]

        password = json.loads(payload)["newPassword"]

        try:
            password_validation.validate_password(password, request.user)
        except ValidationError as e:
            responsePayload = {
                "status": "failure",
                "cause": "guidelineViolation",
                "desc": e.messages[0]
            }
            return Response(responsePayload, status=422)

        request.user.set_password(password)
        request.user.save()
        update_session_auth_hash(request, request.user)

        responsePayload = {
            "status": "success",
            "redirect": resolve_url(settings.LOGIN_REDIRECT_URL)
        }
        return Response(responsePayload, status=200)
