import json
import re

from argon2 import PasswordHasher
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
    try:
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

        # TODO check password

        ph = PasswordHasher()
        password = ph.hash(password)

        user = User.objects.create(email=email, username=username, password=password)
        user.save()
        return HttpResponse(json.dumps({"status": "success"}), status=201)
    except Exception as e:
        print(e)
        return HttpResponse(status=400)


def unsupportedMethod(request):
    return HttpResponse(status=405)
