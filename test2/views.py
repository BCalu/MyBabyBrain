from django.shortcuts import render
from django.http import HttpResponse
from test2.forms import *

# def index(request):
#    template_name = "test2/index.html"
#    return render(request, template_name, {})

# def index_2(request):
#    template_name = "test2/index.html"
#    asdasd
#    a = range(100)
#    print ("asdkljasdklasjdjhaslsdajhk", template_name)

#    return render(request, template_name, {"validar" : True})


def index(request):
    return HttpResponse("Mi primera vista")


def login(request):
    template_name = "test2/Login.html"
    return render(request, template_name)


def prueba(request):
    template_name = "test2/index.html"
    formpersona = AddPersona()
    return render(request, template_name, {"FormPersona": formpersona})
