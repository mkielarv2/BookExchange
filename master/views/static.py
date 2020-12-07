from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from offers.models import Offers


def index(request):
    offers = Offers.objects.all()

    template = loader.get_template('index.html')
    context = {
        'offers': offers,
    }
    return HttpResponse(template.render(context, request))


def login(request):
    return render(request, 'login.html')


def logout(request):
    return render(request, 'logout.html')


def register(request):
    return render(request, 'register.html')


def change(request):
    return render(request, 'change.html')
