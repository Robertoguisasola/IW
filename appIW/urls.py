from django.urls import path, reverse_lazy
from django.contrib import admin
from django.views.generic import RedirectView
from . import views


urlpatterns = [
    path('index', views.index, name='indice'), #portada de la web con dos estaciones por localización
    path('cordillera/<int:cordillera_id>/', views.cordillera, name='cordillera'), #detalles de una cordillera determinada
    path('estacion/<int:estacion_id>/', views.estacion, name='estacion'), #detalles de una estación de esquí
    path('pista/<int:pista_id>/', views.pista, name='pista'), #detalles de una pista
    path('admin/', RedirectView.as_view(url=reverse_lazy('admin:index')), name='admin')
]