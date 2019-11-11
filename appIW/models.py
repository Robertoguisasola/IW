from django.db import models

# Create your models here.

class Provincia(models.Model):
    nombre = models.CharField(max_length=50)

class Estacion(models.Model):
    nombre = models.CharField(max_length=50)
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE)
    nPistas = models.IntegerField()
    nKilometros = models.IntegerField()

class Pista(models.Model):
    estacion = models.ForeignKey(Estacion, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    dificultad = models.CharField(max_length=10)
    longitud = models.IntegerField()
