from django import forms
from .models import Mantenimiento
from datetime import date 

#Definir la clase formulario 

class MantenimientoForm(forms.ModelForm):
    class Meta:
        model = Mantenimiento
        fields = ['vehiculo','fecha', 'observaciones','evidencia_fotografica', 'factura']

# Validacion para los campos de fecha, observacion

def clean_fecha(self):
    fecha = self.cleaned_data.get(fecha)
    if fecha > date.today():
        raise forms.ValidationError("La fecha del mantenimiento no puede ser en el futuro.")
    return fecha

def clean_observaciones(self):
    observaciones = self.cleand_data.get('observaciones')
    if len(observaciones) <10:
        raise forms.ValidationError('Las observaciones deben tener al menos 10 caracteres')
    return observaciones