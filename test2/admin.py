from django.contrib import admin

from test2.models import *
# Register your models here.


@admin.register(Medico)
class MedicoAdmin(admin.ModelAdmin):
    list_display = ('rut', 'nombre', 'apellido')
