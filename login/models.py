from django.db import models


class Credenciales(models.Model):
    usuario = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    permisos = models.CharField(max_length=1,
                                choices=(
                                    ('M', 'Medico'),
                                    ('P', 'Pariente'),
                                ))
