from django import forms
from .models import Asistencia
import re

class AsistenciaForm(forms.ModelForm):
    class Meta:
        model = Asistencia
        fields = [
            'nombre_completo', 'documento', 'correo_electronico',
            'fecha_asistencia', 'hora_ingreso', 'hora_salida',
            'presente', 'observaciones'
        ]
        widgets = {
            'fecha_asistencia': forms.DateInput(attrs={'type': 'date'}),
            'hora_ingreso': forms.TimeInput(attrs={'type': 'time'}),
            'hora_salida': forms.TimeInput(attrs={'type': 'time'}),
            'correo_electronico': forms.EmailInput(attrs={'placeholder': 'ejemplo@dominio.com'}),
            'observaciones': forms.Textarea(attrs={'rows': 3}),
        }

    def clean_documento(self):
        doc = self.cleaned_data.get('documento', '').strip()
        if not re.match(r'^[A-Za-z0-9]+$', doc):
            raise forms.ValidationError('El documento debe ser alfanumérico (sin espacios ni símbolos).')
        return doc

    def clean(self):
        cleaned = super().clean()
        hi = cleaned.get('hora_ingreso')
        hs = cleaned.get('hora_salida')
        if hi and hs and hs < hi:
            raise forms.ValidationError('La hora de salida no puede ser anterior a la hora de ingreso.')
        return cleaned
