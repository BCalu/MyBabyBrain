from django.urls import path
from test2 import views

urlpatterns = [
    #path('asdasdasasdhasjdhj/', views.index, name="iniciiio"),
    #path('index/', views.index_2, name="inicio_2"),
    path('index', views.index, name='index'),
    path('login', views.login, name='login'),
    path('prueba', views.prueba, name='prueba'),
]
