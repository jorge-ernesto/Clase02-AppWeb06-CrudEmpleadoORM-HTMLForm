from django import forms
from app.models import Empleado

class EmpleadoForm(forms.ModelForm):

    class Meta:
        model=Empleado
        fields='__all__'
        