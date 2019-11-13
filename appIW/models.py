from django.db import models


# Create your models here.

class Cordillera(models.Model):
    nombre = models.CharField(max_length=50, default="")


class Estacion(models.Model):
    cordillera = models.ForeignKey(Cordillera, on_delete=models.CASCADE, default="")
    nombre = models.CharField(max_length=50, default="")
    abierta = models.BooleanField(default=False)
    nPistas = models.IntegerField(default=0)
    nPistasTotales = models.IntegerField(default=0)
    nKilometros = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)
    nKilometrosTotales = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)
    enlacePagina = models.CharField(max_length=200, default="")


class Pista(models.Model):
    estacion = models.ForeignKey(Estacion, on_delete=models.CASCADE, default="")
    nombre = models.CharField(max_length=50, default="")
    abierta = models.BooleanField(default=False)
    dificultad = models.CharField(max_length=10, default="Verde")
    longitud = models.DecimalField(max_digits=6, decimal_places=2)
