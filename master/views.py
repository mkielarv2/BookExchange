from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')
    # return HttpResponse("The D is silent.")

def register(request):
    return render(request, 'register.html')