from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Cordillera, Estacion, Pista

admin.site.register(Cordillera)
admin.site.register(Estacion)
admin.site.register(Pista)


