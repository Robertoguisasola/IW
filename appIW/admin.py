from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Provincia, Estacion, Pista
admin.site.register(Provincia)
admin.site.register(Estacion)
admin.site.register(Pista)


