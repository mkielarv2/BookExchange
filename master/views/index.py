from django.http import HttpResponse
from django.template import loader

from offers.models import Offers


def index(request):
    offers = Offers.objects.all()

    template = loader.get_template('index.html')
    context = {
        'offers': offers,
    }
    return HttpResponse(template.render(context, request))
