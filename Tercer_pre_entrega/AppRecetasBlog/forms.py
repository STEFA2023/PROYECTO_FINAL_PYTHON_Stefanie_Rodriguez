from django import forms

# Create your forms here.

class recetas_ingresadas_formulario(forms.Form):
    nombre = forms.CharField(max_length = 50)
    autor = forms.CharField(max_length = 20)
    ingrediente_principal = forms.CharField(max_length = 100)
    ingredientes = forms.CharField()
    procedimiento = forms.CharField(max_length = 2000)
    cantidad_de_comensales = forms.CharField(max_length = 10)