from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages


def portal_login(request):
    template_name = "login/login.html"
    data = {}

    logout(request)
    username = password = ''
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(
            username=username,
            password=password
        )
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('agregar_medico'))
            else:
                messages.warning(
                    request,
                    'USUARIO NO VALIDO'
                )
        else:
            messages.error(
                request,
                'USUARIO INCORRECTO'
            )

    return render(request, template_name, data)


def portal_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))
