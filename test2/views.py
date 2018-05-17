from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
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


# def index(request):
#    return HttpResponse("Mi primera vista")


# def login(request):
#    template_name = "test2/Login.html"
#    return render(request, template_name)


def agregar_medico(request):
    # Si el request es un POST
    if request.POST:
        # Crea objeto con los atributos del POST
        formMedico = AddMedico(request.POST, request.FILES)
        # Si los atributos estan validados correctamente
        if formMedico.is_valid():
            # Crea objeto y lo guarda en la BDD
            Medico = formMedico.save(commit=False)
            # Esta el objeto si necesito trabajar con el
            Medico.save()
        return JsonResponse({"llave": 'VALOR'})
    template_name = "test2/Agregar_Medico.html"
    formMedico = AddMedico()
    return render(request, template_name, {"FormMedico": formMedico})


def agregar_paciente(request):
    template_name = "test2/Agregar_Paciente.html"
    formPaciente = AddPaciente()
    return render(request, template_name, {"FormPaciente": formPaciente})
