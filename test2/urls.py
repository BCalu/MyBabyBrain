from django.urls import path
from test2 import views

# path('url', views.tu_vista, name='nombre_variable')
urlpatterns = [
    path('agregar_medico', views.agregar_medico, name='agregar_medico'),
    path('agregar_paciente', views.agregar_paciente, name='agregar_paciente'),
    path('agregar_pariente', views.agregar_pariente, name='agregar_pariente'),
]
