from django.urls import path, reverse_lazy, include
from django.views.generic import RedirectView
from . import views

# Internacionalizacion para JavaScript
js_info_dict = {
    'domain': 'djangojs',
    'packages': ('wrnpro',),
}

urlpatterns = {
    path(r'index', views.index, name='indice'),  # portada de la web con dos estaciones por localización
    path(r'cordilleras', views.cordilleras, name='cordilleras'),  # todas las cordilleras y sus estaciones
    path(r'cordillera/<int:cordillera_id>/', views.cordillera, name='cordillera'),
    # detalles de una cordillera determinada
    path(r'estaciones', views.estaciones, name='estaciones'),  # todas las estaciones
    path(r'estacion/<int:estacion_id>/', views.estacion, name='estacion'),  # detalles de una estación de esquí
    path(r'pistas', views.pistas, name='pistas'),  # todas las pistas por estacion
    path(r'pista/<int:pista_id>/', views.pista, name='pista'),  # detalles de una pista
    path(r'contacto/', views.contacto, name='contacto'),
    path(r'admin/', RedirectView.as_view(url=reverse_lazy('admin:index')), name='admin'),
    path(r'i18n/', include('django.conf.urls.i18n')),
    path(r'rosetta/', include('rosetta.urls'))
}
