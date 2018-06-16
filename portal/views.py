from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django import template
from portal.forms import AddMedico, AddSupervisor, AddPaciente
from portal.models import Medico, Supervisor, Paciente
from .permisos import usuario_es_admin, usuario_es_medico, usuario_es_supervisor


# funciones supervisor
def ver_ficha_paciente(request):
    pass


def exportar(request):
    pass


# funciones medico (incluyendo las de supervisor)
def listar_pacientes(request):
    pass


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


def editar_paciente(request):
    pass


def editar_ficha_paciente(request):
    pass


@login_required(login_url='/login')
def agregar_supervisor(request):
    if request.method == "POST":
        formSupervisor = AddSupervisor(request.POST, request.FILES)
        if formSupervisor.is_valid():
            Supervisor = formSupervisor.save(commit=False)
            Supervisor.save()
    template_name = "portal/Agregar_Supervisor.html"
    formSupervisor = AddSupervisor()
    return render(request, template_name, {"FormSupervisor": formSupervisor})


def editar_supervisor(request):
    pass


def agregar_usuario_supervisor(request):
    pass


# funciones admin (incluyendo las de supervisor y medico)
@login_required(login_url='/login/')
def agregar_medico(request):
    # Si el request es un POST
    if request.method == "POST":
        # Crea objeto con los atributos del POST
        formMedico = AddMedico(request.POST, request.FILES)
        # Si los atributos estan validados correctamente
        if formMedico.is_valid():
            # Crea objeto y lo guarda en la BDD
            medico = formMedico.save(commit=False)
            # Esta el objeto si necesito trabajar con el
            medico.save()
            user = User.objects.create_user(username=rut,
                                            email=email,
                                            password=fecha_nacimiento)
            grupo = Group.objects.get(name='Medicos')
            grupo.user_set.add(user)
        # return JsonResponse({"llave": 'VALOR'})
    template_name = "portal/Agregar_Medico.html"
    formMedico = AddMedico()
    return render(request, template_name, {"FormMedico": formMedico})


def editar_medico(request):
    pass


def agregar_usuario_medico(request):
    pass
