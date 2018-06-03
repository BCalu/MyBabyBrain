from django.contrib import admin

from test2.models import *
# Register your models here.


@admin.register(Medico)
class MedicoAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'apellidos',)


@admin.register(Pariente)
class ParienteAdmin(admin.ModelAdmin):
    pass


@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    pass
