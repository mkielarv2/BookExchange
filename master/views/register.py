import re

from django.contrib.auth import password_validation
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


class Register(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        payload = request.data

        email = payload["email"]
        username = payload["username"]
        password = payload["password"]

        if not re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)").match(email):
            return Response({"status": "failure", "cause": "emailField", "desc": "Invalid email."}, status=400)
        if User.objects.filter(email=email).exists():
            return Response({"status": "failure", "cause": "emailField", "desc": "Email already in use."}, status=422)
        if User.objects.filter(username=username).exists():
            return Response({"status": "failure", "cause": "usernameField", "desc": "Username already taken."},
                            status=422)

        try:
            password_validation.validate_password(password, request.user)
        except ValidationError as e:
            responsePayload = {
                "status": "failure",
                "cause": "passwordField",
                "desc": e.messages[0]
            }
            return Response(responsePayload, status=422)

        user = User.objects.create(username=username, email=email)
        user.set_password(password)
        user.save()

        return Response({"status": "success"}, status=201)
