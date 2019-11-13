from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, get_list_or_404
from .models import Cordillera, Estacion


# Create your views here.
def index(request):
    cordilleras = get_list_or_404(Cordillera.objects.order_by('nombre'))
    context = {'listaCordilleras':cordilleras}
    return render(request, 'appIW/index.HTML', context)
