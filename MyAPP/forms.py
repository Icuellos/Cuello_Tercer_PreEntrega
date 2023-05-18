from django import forms
from .models import Liga

class CrearNuevoFormulario(forms.Form):
    title = forms.CharField(label="Nombre", max_length=200)
    edad = forms.IntegerField(label="Ingrese su edad")
    title2 = forms.CharField(label="Equipo al que pertenece", max_length=200)
    
    
class CrearNuevoProyecto(forms.Form):
    name = forms.CharField(label="Nombre de equipo", max_length=200)
    
# Eliminar desde aqui en caso de error    
class CrearNuevaLiga(forms.Form):
    name = forms.CharField(label="Nombre de la Liga", max_length=200)    
    

    