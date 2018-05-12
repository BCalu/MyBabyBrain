from django.urls import path
from test2 import views

# path('url', views.tu_vista, name='nombre_variable')
urlpatterns = [
    # path('asdasdasasdhasjdhj/', views.index, name="iniciiio"),
    # path('index/', views.index_2, name="inicio_2"),
    # path('index', views.index, name='index'),
    # path('login', views.login, name='login'),
    path('agregar_medico', views.agregar_medico, name='agregar_medico'),
    path('agregar_paciente', views.agregar_paciente, name='agregar_paciente'),
]
