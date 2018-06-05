from django.db import models
from login.models import Credenciales
from django import forms
from datetime import date
from itertools import cycle

# Crear aqui los modelos. Cada vez que se realice un cambio realizar la migrations
# makemigrations versiona las migraciones
# migrate hace los cambios


class Persona(models.Model):
    rut = models.CharField(max_length=15,
                           help_text="Ejemplo: 12345678-9")
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField(help_text="Formato: AAAA-MM-DD")
    edad = models.PositiveIntegerField()
    nacionalidad = models.CharField(max_length=50)
    region = models.CharField(max_length=70)
    ciudad = models.CharField(max_length=50)
    domicilio = models.CharField(max_length=200)
    genero = models.CharField(max_length=1,
                              choices=(
                                  ('F', 'Femenino'),
                                  ('M', 'Masculino'),
                              ))

    def calcular_edad(self):
        today = date.today()
        self.edad = today.year - fecha_nacimiento.year - ((today.month, today.day) < (fecha_nacimiento.month, fecha_nacimiento.day))

    def validar_rut(self):
        self.rut = self.rut.upper()
        self.rut = self.rut.replace("-", "")
        self.rut = self.rut.replace(".", "")
        aux = self.rut[:-1]
        dv = self.rut[-1:]
        revertido = map(int, reversed(str(aux)))
        factors = cycle(range(2, 8))
        s = sum(d * f for d, f in zip(revertido, factors))
        res = (-s) % 11

        if str(res) == dv:
            return True
        elif dv == "K" and res == 10:
            return True
        else:
            return False

    def __str__(self):
        return self.nombres + " " + self.apellidos


class Medico(Persona):
    usuario_login = models.OneToOneField(Credenciales,
                                         on_delete=models.CASCADE,
                                         null=True)
    logo = models.ImageField(upload_to='ImagenesMedicos/')
    email = models.EmailField(max_length=120,
                              null=True,
                              blank=True)
    telefono_celular = models.CharField(max_length=13,
                                        null=True,
                                        blank=True)
    telefono_domiclio = models.CharField(max_length=13,
                                         null=True,
                                         blank=True)


class Pariente(Persona):
    usuario_login = models.OneToOneField(Credenciales,
                                         on_delete=models.CASCADE,
                                         null=True)
    ocupacion = models.CharField(max_length=100,
                                 blank=True)
    estado_civil = models.CharField(max_length=2,
                                    choices=(
                                        ('SO', 'Soltero/a'),
                                        ('C', 'Casado/a'),
                                        ('V', 'Viudo/a'),
                                        ('D', 'Divorciado/a'),
                                        ('SE', 'Separado/a'),
                                    ))
    email = models.EmailField(max_length=120,
                              null=True,
                              blank=True)
    telefono_celular = models.CharField(max_length=13,
                                        null=True,
                                        blank=True)
    telefono_domiclio = models.CharField(max_length=13,
                                         null=True,
                                         blank=True)


class Paciente(Persona):
    medico_asignado = models.ForeignKey(Medico,
                                        on_delete=models.CASCADE)
    parientes = models.ForeignKey(Pariente,
                                  on_delete=models.CASCADE)
    alergias = models.TextField(max_length=300)
    enfermedades = models.TextField(max_length=300)
    operaciones = models.TextField(max_length=300)
    farmacos = models.TextField(max_length=300)
    hospitalizaciones = models.TextField(max_length=300)
