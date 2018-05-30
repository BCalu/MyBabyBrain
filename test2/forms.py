from django.forms import ModelForm
from test2.models import Medico, Pariente, Paciente


class AddMedico(ModelForm):
    class Meta():
        model = Medico
        fields = ['logo', 'email', 'telefono_celular', 'telefono_domiclio']


class addPariente(ModelForm):
    class Meta():
        model = Pariente
        fields = ['email', 'telefono_celular', 'telefono_domiclio']


class AddPaciente(ModelForm):
    class Meta():
        model = Paciente
        fields = ['medico_asignado', 'parientes', 'alergias', 'enfermedades',
                  'operaciones', 'farmacos', 'hospitalizaciones']
