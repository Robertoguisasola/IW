from django.contrib import admin
from .models import Cordillera, Estacion, Pista

# Register your models here.

admin.site.register(Cordillera)


class EstacionAdmin(admin.ModelAdmin):
    fields = ['nombre', 'cordillera', 'enlacePagina', 'nPistasTotales', 'nKilometrosTotales']


class PistaAdmin(admin.ModelAdmin):
    fields = ['estacion', 'nombre', 'dificultad', 'longitud', 'abierta']


admin.site.register(Estacion, EstacionAdmin)
admin.site.register(Pista, PistaAdmin)
