#FORMULARIOS BRINDADOS POR Django
#? Ventaja: alta velocidad de cracion de formularios y una alta efectividad en el proceso de VALIDACION del formulario junto con la flexibilidad de los campos

#! Mas complicado generarle ESTILOS, ya que vienen PREDETERMINADOS con los html

from django import forms
from .models import Productos

#creamos una CLASE QUE HEREDE LAS PROPIEDADES DEL FORM
class FormProductos(forms.ModelForm):
    
    #importacion de MODELO: TRAER TODOS LOS CAMPOS NECESARIOS DE UN MODEL CREADO
    class Meta:
        model = Productos
        fields = '__all__'