import json

from django.conf import settings
from django.contrib.auth import authenticate
from django.contrib.auth import login as authLogin
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import resolve_url, render


def login(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return HttpResponseRedirect(resolve_url(settings.LOGIN_REDIRECT_URL))
        return page(request)
    elif request.method == 'POST':
        return authorize(request)
    else:
        return unsupportedMethod(request)


def page(request):
    return render(request, "login.html")


def authorize(request):
    payload = json.loads(request.POST["payload"])

    username = payload["username"]
    password = payload["password"]

    user = authenticate(request, username=username, password=password)

    if user is None:
        responsePayload = {
            "status": "failure",
            "cause": "credentials",
            "desc": "Invalid user or password."
        }
        return HttpResponse(json.dumps(responsePayload), status=401)

    authLogin(request, user)

    responsePayload = {
        "status": "success",
        "redirect": resolve_url(settings.LOGIN_REDIRECT_URL)
    }
    return HttpResponse(json.dumps(responsePayload), status=200)


def unsupportedMethod(request):
    return HttpResponse(status=405)
