from django.urls import path, reverse_lazy
from django.contrib import admin
from django.views.generic import RedirectView
from . import views


urlpatterns = [
    path('index', views.index, name='indice'),
    path('cordillera/<int:cordillera_id>/', views.cordillera, name='cordillera'),
    path('estacion/<int:estacion_id>/', views.estacion, name='estacion'),
    path('pista/<int:pista_id>/', views.pista, name='pista'),
    path('admin/', RedirectView.as_view(url=reverse_lazy('admin:index')), name='admin')
]