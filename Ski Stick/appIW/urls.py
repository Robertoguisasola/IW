from django.urls import path, reverse_lazy
from django.views.generic import RedirectView
from . import views


urlpatterns = [
    path('index', views.index, name='indice'), #portada de la web con dos estaciones por localización
    path('cordilleras', views.cordilleras, name='cordilleras'), # todas las cordilleras y sus estaciones
    path('cordillera/<int:cordillera_id>/', views.cordillera, name='cordillera'), #detalles de una cordillera determinada
    path('estaciones', views.estaciones, name='estaciones'), #todas las estaciones
    path('estacion/<int:estacion_id>/', views.estacion, name='estacion'), #detalles de una estación de esquí
    path('pistas', views.pistas, name='pistas'), #todas las pistas por estacion
    path('pista/<int:pista_id>/', views.pista, name='pista'), #detalles de una pista
    path('contacto/', views.contacto, name='contacto'),
    path('admin/', RedirectView.as_view(url=reverse_lazy('admin:index')), name='admin')

]