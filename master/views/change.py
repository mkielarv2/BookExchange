import json

from django.conf import settings
from django.contrib.auth import authenticate, update_session_auth_hash, password_validation
from django.contrib.auth import login as authLogin
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import resolve_url, render


def change(request):
    if request.method == 'GET':
        if not request.user.is_authenticated:
            return HttpResponseRedirect("/login")
        return page(request)
    elif request.method == 'POST':
        return changeHash(request)
    else:
        return unsupportedMethod(request)


def page(request):
    return render(request, "change.html")


def changeHash(request):
    payload = json.loads(request.POST["payload"])

    password = payload["newPassword"]

    try:
        password_validation.validate_password(password, request.user)
    except ValidationError as e:
        responsePayload = {
            "status": "failure",
            "cause": "guidelineViolation",
            "desc": e.messages[0]
        }
        return HttpResponse(json.dumps(responsePayload), status=422)

    request.user.set_password(password)
    request.user.save()
    update_session_auth_hash(request, request.user)

    responsePayload = {
        "status": "success",
        "redirect": resolve_url(settings.LOGIN_REDIRECT_URL)
    }
    return HttpResponse(json.dumps(responsePayload), status=200)


def unsupportedMethod(request):
    return HttpResponse(status=405)
