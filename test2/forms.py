from django import forms
from test2.models import *


class AddMedico(forms.ModelForm):
    class Meta():
        model = Medico
        widgets = {
            'rut': forms.TextInput(attrs={'class': 'form-control col-md-7 col-xs-12',
                                          'placeholder': 'Ingrese Rut'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control col-md-7 col-xs-12',
                                             'placeholder': 'Ingrese Nombre'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control col-md-7 col-xs-12',
                                               'placeholder': 'Ingrese Apellido'}),
            'fecha_nacimiento': forms.DateInput(attrs={'class': 'form-control col-md-7 col-xs-12',
                                                       'placeholder': 'YY-MM-DD'}),
            'email': forms.EmailInput(attrs={'class': 'form-control col-md-7 col-xs-12',
                                             'placeholder': 'Ingrese Correo Electronico'})
        }
        exclude = []
        # fields = []


class AddPaciente(forms.ModelForm):
    class Meta():
        model = Paciente
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control col-md-7 col-xs-12',
                                             'placeholder': 'Ingrese Nombre'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control col-md-7 col-xs-12',
                                               'placeholder': 'Ingrese Apellido'}),
            'fecha_nacimiento': forms.DateInput(attrs={'class': 'form-control col-md-7 col-xs-12',
                                                       'placeholder': 'YY-MM-DD'}),
        }
        exclude = []
        # fields = []
