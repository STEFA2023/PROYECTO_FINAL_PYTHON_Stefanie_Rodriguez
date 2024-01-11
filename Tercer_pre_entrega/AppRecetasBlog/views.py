from django.shortcuts import render
from AppRecetasBlog.models import recetas_ingresadas
from AppRecetasBlog.forms import recetas_ingresadas_formulario

# Create your views here.

def agregar_receta(request):

    if request.method=="POST":

        info_formulario_recetas = recetas_ingresadas_formulario(request.POST)
        if info_formulario_recetas.is_valid():

            info = info_formulario_recetas.cleaned_data

            nueva_receta = recetas_ingresadas(nombre=info["nombre"], autor=info["autor"], ingrediente_principal=info["ingrediente_principal"], ingredientes=info["ingredientes"], procedimiento=info["procedimiento"], cantidad_de_comensales=info["cantidad_de_comensales"])

            nueva_receta.save()

            return render(request, "recetas.html")

    else:
        nuevo_formulario_recetas = recetas_ingresadas_formulario()

    formulario_de_ingreso = recetas_ingresadas_formulario()

    return render(request, "creador_de_recetas.html", {"formulario":formulario_de_ingreso})


def ver_recetas_ingresadas(request):


    return render(request, "recetas.html")