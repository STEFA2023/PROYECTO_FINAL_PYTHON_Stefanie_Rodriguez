from django import forms

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
    nombre = forms.CharField(max_length = 50)
    apellido = forms.CharField(max_length = 50)
    edad = forms.IntegerField()
    email = forms.EmailField()
    pais = forms.CharField(max_length = 2000)
    fecha_de_nacimiento = forms.DateField()