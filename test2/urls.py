from django.urls import path
from test2 import views

urlpatterns = [
    path('asdasdasasdhasjdhj/', views.index, name="iniciiio"),
    path('index/', views.index_2, name="inicio_2"),

]
