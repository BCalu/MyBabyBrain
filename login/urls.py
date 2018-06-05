from django.urls import path
from login import views

urlpatterns = [
    path('', views.portal_login, name="login"),
    path('logout', views.portal_logout, name="logout"),
]
