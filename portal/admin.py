from django.contrib import admin

from portal.models import Medico, Supervisor, Paciente
# Register your models here.


@admin.register(Medico)
class MedicoAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'apellidos',)


@admin.register(Supervisor)
class SupervisorAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'apellidos',)


@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'apellidos', 'medico_asignado', 'supervisor_asignado')