from django.forms import ModelForm
from test2.models import Medico, Paciente


class AddMedico(ModelForm):
    class Meta():
        model = Medico
        fields = []


class AddPaciente(ModelForm):
    class Meta():
        model = Paciente
        fields = []
