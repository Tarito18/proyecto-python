from django import forms

class empleadoForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    edad = forms.IntegerField()
    cargo = forms.CharField(max_length=50)


class pedidoForm(forms.Form):
    cliente = forms.CharField(max_length=50)
    empleado = forms.CharField(max_length=50)
    fecha = forms.DateField()