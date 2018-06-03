from django.forms import ModelForm
from test2.models import Medico, Pariente, Paciente


class AddMedico(ModelForm):
    class Meta():
        model = Medico
        fields = ['rut', 'nombres', 'apellidos', 'fecha_nacimiento', 'edad',
                  'nacionalidad', 'region', 'ciudad', 'domicilio', 'genero',
                  'logo', 'email', 'telefono_celular', 'telefono_domiclio']


class AddPariente(ModelForm):
    class Meta():
        model = Pariente
        fields = ['rut', 'nombres', 'apellidos', 'fecha_nacimiento', 'edad',
                  'nacionalidad', 'region', 'ciudad', 'domicilio', 'genero',
                  'estado_civil', 'ocupacion', 'email', 'telefono_celular',
                  'telefono_domiclio']


class AddPaciente(ModelForm):
    class Meta():
        model = Paciente
        fields = ['rut', 'nombres', 'apellidos', 'fecha_nacimiento', 'edad',
                  'nacionalidad', 'region', 'ciudad', 'domicilio', 'genero',
                  'medico_asignado', 'parientes', 'alergias', 'enfermedades',
                  'operaciones', 'farmacos', 'hospitalizaciones']
