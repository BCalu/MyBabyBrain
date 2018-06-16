from django.urls import path
from portal import views

# path('url', views.tu_vista, name='nombre_variable')
urlpatterns = [
    # funciones supervisor
    path('ficha/paciente/<int:paciente_rut>',
         views.ver_ficha_paciente,
         name='ver_ficha_paciente'),
    path('exportar',
         views.exportar,
         name='exportar'),
    # funciones medico (incluyendo las de supervisor)
    path('pacientes',
         views.listar_pacientes,
         name='listar_pacientes'),
    path('agregar/paciente',
         views.agregar_paciente,
         name='agregar_paciente'),
    path('editar/paciente/<int:paciente_rut>',
         views.editar_paciente,
         name='editar_paciente'),
    path('editar/ficha/paciente/<int:paciente_rut>',
         views.editar_ficha_paciente,
         name='editar_ficha_paciente'),
    path('agregar/supervisor',
         views.agregar_supervisor,
         name='agregar_supervisor'),
    path('editar/supervisor/<int:supervisor_rut>',
         views.editar_supervisor,
         name='editar_supervisor'),
    path('agregar/usuario/supervisor',
         views.agregar_usuario_supervisor,
         name='agregar_usuario_supervisor'),
    # funciones admin (incluyendo las de supervisor y medico)
    path('agregar/medico',
         views.agregar_medico,
         name='agregar_medico'),
    path('editar/medico/<int:medico_rut>',
         views.editar_medico,
         name='editar_medico'),
    path('agregar/usuario/medico',
         views.agregar_usuario_medico,
         name='agregar_usuario_medico'),
]
