from django.urls import path
from portal import views

# path('url', views.tu_vista, name='nombre_variable')
urlpatterns = [
    path('agregar_medico', views.agregar_medico, name='agregar_medico'),
    path('agregar_paciente', views.agregar_paciente, name='agregar_paciente'),
    path('agregar_supervisor', views.agregar_supervisor, name='agregar_supervisor'),
]
