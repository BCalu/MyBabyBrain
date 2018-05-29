from django.contrib import admin

from test2.models import *
# Register your models here.


@admin.register(Medico)
class MedicoAdmin(admin.ModelAdmin):
    pass


@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    pass
