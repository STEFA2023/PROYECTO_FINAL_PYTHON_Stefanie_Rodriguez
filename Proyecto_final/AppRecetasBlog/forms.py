from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils import timezone
from .models import ingreso_al_blog
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

#form regitro de usuario:
    
class UserCreationForm(UserCreationForm):
    email: forms.EmailField()
    password1: forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2: forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_text = {k:"" for k in fields}

#forms Ingreso blog libre
    
class formulario_ingreso_al_blog(forms.ModelForm):
    titulo = forms.CharField(max_length=500)
    fecha = forms.DateTimeField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fecha'].initial = timezone.now()

    class Meta:
        model = ingreso_al_blog
        fields = ['titulo', 'tema', 'historia']

#forms Contacto

class formulario_de_contacto(forms.Form):
    Nombre_Completo = forms.CharField(max_length= 100)
    email = forms.EmailField()
    consulta = forms.CharField(max_length= 6000)