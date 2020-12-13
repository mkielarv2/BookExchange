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


def create(request):
    return render(request, 'create.html')


# ----------------------------------------------------------------

def registerTab(request):
    return render(request, 'register_tab.html')


def loginTab(request):
    return render(request, 'login_tab.html')


def productTab(request):
    return render(request, 'product_tab.html')


def shopTab(request):
    return render(request, 'shop_tab.html')


def sorting(request):
    return render(request, 'sorting.html')


def userProducts(request):
    return render(request, 'user_products.html')
