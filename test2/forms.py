from django import forms
from test2.models import *


class AddPersona(forms.ModelForm):
    class Meta():
        model = Persona
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control col-md-7 col-xs-12',
                                             'placeholder': 'Ingrese Nombre'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control col-md-7 col-xs-12',
                                               'placeholder': 'Ingrese Apellido'}),
            'estado_social': forms.Select(attrs={'class': 'form-control', })
        }
        exclude = []
        # fields = []
