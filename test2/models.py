from django.db import models
from django import forms

# Crear aqui los modelos. Cada vez que se realice un cambio realizar la migrations
# makemigrations versiona las migraciones
# migrate hace los cambios


class Medico(models.Model):
    rut = models.CharField(max_length=15)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    email = models.EmailField(max_length=120)


class Paciente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
