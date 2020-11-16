from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


def index(request):
    offers = {
        ("Lalka", "Bolesław Prus", 1890),
        ("Zbrodnia i kara", "Fiodor Dostojewski", 1887),
        ("Chłopi", "Władysław Reymont", 1904),
        ("Krzyżacy", "Henryk Sienkiewicz", 1901),
        ("Dziady część III", "Adam Mickiewicz", 1845),
        ("Antygona", "Sofokles", 1993)
    }

    template = loader.get_template('index.html')
    context = {
        'offers': offers,
    }
    return HttpResponse(template.render(context, request))

    # return render(request, 'index.html')
    # return HttpResponse("The D is silent.")


def register(request):
    return render(request, 'register.html')


def login(request):
    return render(request, 'login.html')
