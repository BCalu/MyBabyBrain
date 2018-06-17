from django.forms import ModelForm
from django.contrib.auth.models import User, Group
from portal.models import Administrador, Medico, Supervisor, Paciente


class AddAdministrador(ModelForm):
    class Meta():
        model = Administrador
        fields = ['rut', 'nombres', 'apellidos', 'fecha_nacimiento',
                  'nacionalidad', 'region', 'ciudad', 'domicilio', 'genero',
                  'email', 'telefono_celular', 'telefono_domiclio']


class AddMedico(ModelForm):
    class Meta():
        model = Medico
        fields = ['rut', 'nombres', 'apellidos', 'fecha_nacimiento',
                  'nacionalidad', 'region', 'ciudad', 'domicilio', 'genero',
                  'logo', 'email', 'telefono_celular', 'telefono_domiclio']


class AddSupervisor(ModelForm):
    class Meta():
        model = Supervisor
        fields = ['rut', 'nombres', 'apellidos', 'fecha_nacimiento',
                  'nacionalidad', 'region', 'ciudad', 'domicilio', 'genero',
                  'estado_civil', 'ocupacion', 'email', 'telefono_celular',
                  'telefono_domiclio']


class AddPaciente(ModelForm):
    class Meta():
        model = Paciente
        fields = ['rut', 'nombres', 'apellidos', 'fecha_nacimiento',
                  'nacionalidad', 'region', 'ciudad', 'domicilio', 'genero',
                  'medico_asignado', 'supervisor_asignado', 'alergias',
                  'enfermedades', 'operaciones', 'farmacos', 'hospitalizaciones']
