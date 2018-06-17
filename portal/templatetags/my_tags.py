from django.contrib.auth.models import User, Group
from django import template

register = template.Library()


# FUNCIONES PARA COMPROBAR LOS PERMISOS DE LOS USUARIOS
@register.filter(name='is_admin')
def usuario_es_admin(self):
    admin = self.groups.filter(name='Administradores').exists()
    return True if admin else False


@register.filter(name='is_medico')
def usuario_es_medico(self):
    medico = self.groups.filter(name='Medicos').exists()
    return True if medico else False


@register.filter(name='is_supervisor')
def usuario_es_supervisor(self):
    supervisor = self.groups.filter(name='Supervisores').exists()
    return True if supervisor else False
