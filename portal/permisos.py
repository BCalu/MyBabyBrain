from django.contrib.auth.models import User, Group
from django import template

register = template.Library()


# FUNCIONES PARA COMPROBAR LOS PERMISOS DE LOS USUARIOS
@register.filter(name='es_admin')
def usuario_es_admin(request):
    superuser = request.user.is_superuser
    # BOOLEAN
    admin = request.user.groups.filter(name='Admins').exists()
    return True if superuser and admin else False


@register.filter(name='es_medico')
def usuario_es_medico(request):
    medico = request.user.groups.filter(name='Medicos').exists()
    return True if medico else False


@register.filter(name='es_supervisor')
def usuario_es_supervisor(request):
    supervisor = request.user.groups.filter(name='Supervisores').exists()
    return True if supervisor else False
