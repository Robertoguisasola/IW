from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, get_list_or_404
from .models import Cordillera, Estacion, Pista
from django.utils.translation import gettext


# Create your views here.

# view inicial, saca las cordilleras alfabéticamente y las estaciones descendentes por kilómetros totales
def index(request):
    cordilleras = get_list_or_404(Cordillera.objects.order_by('nombre'))
    estaciones = get_list_or_404(Estacion.objects.order_by('-nKilometrosTotales'))
    estacionesAbiertas = list()
    for estacion in estaciones:
        if estacion.abierta:
            estacionesAbiertas.append(estacion)

    context = {'listaCordilleras': cordilleras, 'listaEstaciones': estacionesAbiertas}
    return render(request, 'appIW/index.HTML', context)


# Devuelve las cordilleras
def cordilleras(request):
    cordilleras = get_list_or_404(Cordillera.objects.order_by('nombre'))
    estaciones = get_list_or_404(Estacion.objects.order_by('-nKilometrosTotales'))
    context = {'listaCordilleras': cordilleras, 'listaEstaciones': estaciones}
    return render(request, 'appIW/cordilleras.html', context)


# Devuelve los detalles de una cordillera
def cordillera(request, cordillera_id):
    cordillera = get_object_or_404(Cordillera, pk=cordillera_id)
    estaciones = cordillera.estacion_set.all()
    context = {'cordillera': cordillera, 'estaciones': estaciones}
    return render(request, 'appIW/cordillera.html', context)


# Devuelve los detalles de una estacion
def estaciones(request):
    estaciones = get_list_or_404(Estacion.objects.order_by('-nKilometrosTotales'))
    context = {'estaciones': estaciones}
    return render(request, 'appIW/estaciones.html', context)


# Devuelve los detalles de una estacion
def estacion(request, estacion_id):
    estacion = get_object_or_404(Estacion, pk=estacion_id)
    pistas = estacion.pista_set.all()
    context = {'estacion': estacion, 'listaPistas': pistas}
    return render(request, 'appIW/estacion.html', context)


# Devuelve todas las pistas por cada estación
def pistas(request):
    estaciones = get_list_or_404(Estacion.objects.order_by('-nKilometrosTotales'))
    pistas = get_list_or_404(Pista.objects.order_by('nombre'))
    context = {'listaEstaciones': estaciones, 'listaPistas': pistas}
    return render(request, 'appIW/pistas.html', context)


# Devuelve los detalles de una pista
def pista(request, pista_id):
    pista = get_object_or_404(Pista, pk=pista_id)
    context = {'pista': pista}
    return render(request, 'appIW/pista.html', context)


def contacto(request):
    return render(request, 'appIW/contacto.html')
