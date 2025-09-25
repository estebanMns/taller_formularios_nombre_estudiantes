from django import forms
from .models import Solicitud

class SolicitudForm(forms.ModelForm):
    """
    Formulario basado en el modelo Solicitud.
    """
    class Meta:
        model = Solicitud
        fields = '__all__'