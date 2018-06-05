from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from test2.forms import AddMedico, AddPariente, AddPaciente
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login/')
def agregar_medico(request):
    # Si el request es un POST
    if request.method == "POST":
        # Crea objeto con los atributos del POST
        formMedico = AddMedico(request.POST, request.FILES)
        # Si los atributos estan validados correctamente
        if formMedico.is_valid():
            # Crea objeto y lo guarda en la BDD
            Medico = formMedico.save(commit=False)
            # Esta el objeto si necesito trabajar con el
            Medico.save()
        # return JsonResponse({"llave": 'VALOR'})
    template_name = "test2/Agregar_Medico.html"
    formMedico = AddMedico()
    return render(request, template_name, {"FormMedico": formMedico})


@login_required(login_url='/login/')
def agregar_paciente(request):
    if request.method == "POST":
        formPaciente = AddPaciente(request.POST, request.FILES)
        if formPaciente.is_valid():
            Paciente = formPaciente.save(commit=False)
            Paciente.save()
    template_name = "test2/Agregar_Paciente.html"
    formPaciente = AddPaciente()
    return render(request, template_name, {"FormPaciente": formPaciente})


@login_required(login_url='/auth/login')
def agregar_pariente(request):
    if request.method == "POST":
        formPariente = AddPariente(request.POST, request.FILES)
        if formPariente.is_valid():
            Pariente = formPariente.save(commit=False)
            Pariente.save()
    template_name = "test2/Agregar_Pariente.html"
    formPariente = AddPariente()
    return render(request, template_name, {"FormPariente": formPariente})
