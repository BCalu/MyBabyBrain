from django.db import models

# Create your models here.


class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    estado_social = models.CharField(max_length=1,
                                     choices=(
                                         ("S", "Soltero"),
                                         ("C", "Casado"),
                                         ("D", "Divorsiado"),
                                         ("O", "Otro"),)
                                     )
