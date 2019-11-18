from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, get_list_or_404
from .models import Cordillera, Estacion, Pista


# Create your views here.
# view inicial
def index(request):
    return render(request, 'appIW/index.html')


def index(request):
    cordilleras = get_list_or_404(Cordillera.objects.order_by('nombre'))
    context = {'listaCordilleras': cordilleras}
    return render(request, 'appIW/index.HTML', context)



# Devuelve los detalles de una cordillera
def cordillera(request, cordillera_id):
    cordillera = get_object_or_404(Cordillera, pk=cordillera_id)
    estaciones = cordillera.estacion_set.all()
    context = {'cordillera': cordillera, 'estaciones': estaciones}
    return render(request, 'appIW/cordillera.html', context)


# Devuelve los detalles de una estacion
def estacion(request, estacion_id):
    estacion = get_object_or_404(Estacion, pk=estacion_id)
    pistas = estacion.pista_set.all()
    context = {'estacion': estacion, 'pistas': pistas}
    return render(request, 'appIW/estacion.html', context)


# Devuelve los detalles de una pista
def pista(request, pista_id):
    pista = get_object_or_404(Pista, pk=pista_id)
    context = {'pista': pista}
    return render(request, 'appIW/pista.html', context)
