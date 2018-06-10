from django.forms import ModelForm
from portal.models import Medico, Supervisor, Paciente


class AddMedico(ModelForm):
    class Meta():
        model = Medico
        fields = ['rut', 'nombres', 'apellidos', 'fecha_nacimiento', 'edad',
                  'nacionalidad', 'region', 'ciudad', 'domicilio', 'genero',
                  'logo', 'email', 'telefono_celular', 'telefono_domiclio']


class AddSupervisor(ModelForm):
    class Meta():
        model = Supervisor
        fields = ['rut', 'nombres', 'apellidos', 'fecha_nacimiento', 'edad',
                  'nacionalidad', 'region', 'ciudad', 'domicilio', 'genero',
                  'estado_civil', 'ocupacion', 'email', 'telefono_celular',
                  'telefono_domiclio']


class AddPaciente(ModelForm):
    class Meta():
        model = Paciente
        fields = ['rut', 'nombres', 'apellidos', 'fecha_nacimiento', 'edad',
                  'nacionalidad', 'region', 'ciudad', 'domicilio', 'genero',
                  'medico_asignado', 'supervisor_asignado', 'alergias',
                  'enfermedades', 'operaciones', 'farmacos', 'hospitalizaciones']
