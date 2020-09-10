from django import forms
from .models import Reserva

class reservaform(forms.ModelForm):
    class Meta:
        model = Reserva 

        fields = [
            'nombre',
            'apellido',
            'fecha',
            'numero_comensales'
        ]

        labels = {
            'nombre': 'Nombre',
            'apellido':'Apellido',
            'fecha':'Fecha',
            'numero_comensales':'Numero Comensales',
        }

        widgtes = {
            'nombre': forms.TextInput(attrs = {'class':'form-control'}),
            'apellido': forms.TextInput(attrs = {'class':'form-control'}),
            'fecha': forms.TextInput(attrs = {'class':'form-control '}),
            'numero_comensales': forms.TextInput(attrs = {'class':'form-control'})
        }