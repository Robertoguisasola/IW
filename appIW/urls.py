from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:cordillera_id>/', views.estacionesLista, name='EstacionesLista'),

]