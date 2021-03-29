from django import forms

class FormRegister(forms.Form):
    usuario = forms.CharField()
    nombre = forms.CharField()
    apellido = forms.CharField()
    correo = forms.EmailField()
    genero = forms.CharField()
    clave = forms.CharField()
    
        
