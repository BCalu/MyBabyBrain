from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from portal.forms import AddMedico, AddSupervisor, AddPaciente
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
    template_name = "portal/Agregar_Medico.html"
    formMedico = AddMedico()
    return render(request, template_name, {"FormMedico": formMedico})


@login_required(login_url='/login/')
def agregar_paciente(request):
    if request.method == "POST":
        formPaciente = AddPaciente(request.POST, request.FILES)
        if formPaciente.is_valid():
            Paciente = formPaciente.save(commit=False)
            Paciente.save()
    template_name = "portal/Agregar_Paciente.html"
    formPaciente = AddPaciente()
    return render(request, template_name, {"FormPaciente": formPaciente})


@login_required(login_url='/auth/login')
def agregar_supervisor(request):
    if request.method == "POST":
        formSupervisor = AddSupervisor(request.POST, request.FILES)
        if formSupervisor.is_valid():
            Supervisor = formSupervisor.save(commit=False)
            Supervisor.save()
    template_name = "portal/Agregar_Supervisor.html"
    formSupervisor = AddSupervisor()
    return render(request, template_name, {"FormSupervisor": formSupervisor})
