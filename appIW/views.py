from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, get_list_or_404
from .models import Provincia, Pista, Estacion


# Create your views here.
def index(request):
    listaProvincias = get_list_or_404(Provincia.objects.order_by('nombre'))
    context = {'provincias': listaProvincias}
    #TODO enlazar estaciones a provincias
    listaEstaciones = get_list_or_404(Estacion.objects.order_by('provincia'))
    context2 = {'estaciones': listaEstaciones}
    return render(request, 'appIW/index.html', context, context2)
