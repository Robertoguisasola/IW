from django.urls import path, reverse_lazy
from django.contrib import admin
from django.views.generic import RedirectView
from . import views


urlpatterns = [
    path('home/', views.index, name='indice'),
    path('/', views.cordilleras, name ='cordilleras'),
    path('<int:cordillera_id>/', views.cordillera, name='cordillera'),
    path('<int:cordillera_id>/', views.estaciones, name='estaciones'),
    path('<int:estacion_id>/', views.estacion, name='estacion'),
    path('<int:estacion_id>/', views.pistas, name='pistas'),
    path('<int:pista_id>/', views.pista, name='pista'),
    path('admin/', RedirectView.as_view(url=reverse_lazy('admin:index')), name='admin')
]