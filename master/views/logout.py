from django.contrib.auth import logout as authLogout
from django.http import HttpResponse
from django.shortcuts import render


def logout(request):
    if request.method == 'GET':
        authLogout(request)
        return render(request, "logout.html")
    else:
        return unsupportedMethod(request)


def unsupportedMethod(request):
    return HttpResponse(status=405)
