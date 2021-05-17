from django import forms
from base.models import *

class ImplementosForm(forms.ModelForm):

    class Meta:
        model = Implemento()

        fields = [
            'id',
            'implemento',
            'estudiante',
            'hora_despacho',
            'hora'
        ]