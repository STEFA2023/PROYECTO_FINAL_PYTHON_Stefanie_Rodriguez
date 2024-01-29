from django import forms
from .models import recetas_ingresadas
# Create your forms here.

#forms recetas ingresadas

class recetas_ingresadas_formulario(forms.Form):
    
    nombre = forms.CharField(max_length = 50)
    autor = forms.CharField(max_length = 20)
    ingrediente_principal = forms.CharField(max_length = 100)
    ingredientes = forms.CharField()
    procedimiento = forms.CharField(max_length = 2000)
    cantidad_de_comensales = forms.CharField(max_length = 10)

#forms usuario ingresado
    
class formulario_usuario_ingresado(forms.Form):
    usuario = forms.CharField(max_length=100)
    nombre = forms.CharField(max_length = 50)
    apellido = forms.CharField(max_length = 50)
    edad = forms.IntegerField()
    email = forms.EmailField()
    pais = forms.CharField(max_length = 2000)
    fecha_de_nacimiento = forms.DateField()
    contraseña1 = forms.CharField(label= "Contraseña",widget=forms.PasswordInput)
    contraseña2 = forms.CharField(label="Repetir la contraseña", widget=forms.PasswordInput)

#forms Ingreso blog libre
    
class formulario_ingreso_al_blog(forms.Form):
    titulo = forms.CharField(max_length=500)
    tema = forms.CharField(max_length=1000)
    historia = forms.CharField(max_length= 6000)

#forms Contacto

class formulario_de_contacto(forms.Form):
    Nombre_Completo = forms.CharField(max_length= 100)
    email = forms.EmailField()
    consulta = forms.CharField(max_length= 6000)