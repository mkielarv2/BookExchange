import json
import re

from django.contrib.auth import get_user_model
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User


def register(request):
    if request.method == 'GET':
        return page(request)
    elif request.method == 'POST':
        return create(request)
    else:
        return unsupportedMethod(request)


def page(request):
    return render(request, 'register.html')


def create(request):
    payload = json.loads(request.POST["payload"])

    email = payload["email"]
    username = payload["username"]
    password = payload["password"]

    if not re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)").match(email):
        return HttpResponse(json.dumps({"cause": "emailField", "desc": "Invalid email."}), status=400)
    if User.objects.filter(email=email).exists():
        return HttpResponse(json.dumps({"cause": "emailField", "desc": "Email already in use."}), status=422)
    if User.objects.filter(username=username).exists():
        return HttpResponse(json.dumps({"cause": "usernameField", "desc": "Username already taken."}), status=422)

    try:
        password_validation.validate_password(password, request.user)
    except ValidationError as e:
        responsePayload = {
            "status": "failure",
            "cause": "passwordField",
            "desc": e.messages[0]
        }
        return HttpResponse(json.dumps(responsePayload), status=422)

    user = User.objects.create(username=username, email=email)
    user.set_password(password)
    user.save()

    return HttpResponse(json.dumps({"status": "success"}), status=201)


def unsupportedMethod(request):
    return HttpResponse(status=405)
