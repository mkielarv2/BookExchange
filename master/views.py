from django.http import HttpResponse


def index(request):
    return HttpResponse("The D is silent.")
