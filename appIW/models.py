from django.db import models


# Create your models here.

class Cordillera(models.Model):
    nombre = models.CharField(max_length=50)


class Estacion(models.Model):
    cordillera = models.ForeignKey(Cordillera, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    abierta = models.BooleanField()
    nPistas = models.IntegerField()
    nPistasTotales = models.IntegerField()
    nKilometros = models.DecimalField(decimal_places=2, max_digits=6)
    nKilometrosTotales = models.DecimalField(decimal_places=2, max_digits=6)
    enlacePagina = models.CharField(max_length=200)


class Pista(models.Model):
    estacion = models.ForeignKey(Estacion, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    abierta = models.BooleanField()
    dificultad = models.CharField(max_length=10)
    longitud = models.DecimalField(decimal_places=2, max_digits=6)
