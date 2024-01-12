from django.shortcuts import render
from AppRecetasBlog.models import recetas_ingresadas
from AppRecetasBlog.forms import recetas_ingresadas_formulario
from AppRecetasBlog.models import usuario_ingresado
from AppRecetasBlog.forms import formulario_usuario_ingresado

# Create your views here.

#Views Ingreso de recetas

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


#Views Ingreso de Usuarios

def agregar_usuario(request):

    if request.method=="POST":

        info_form_usuario_ingresado = formulario_usuario_ingresado(request.POST)
        if info_form_usuario_ingresado.is_valid():

            info = info_form_usuario_ingresado.cleaned_data

            nuevo_usuario = usuario_ingresado(nombre=info["nombre"], apellido=info["apellido"], edad=info["edad"], email=info["email"], pais=info["pais"], fecha_de_nacimiento=info["fecha_de_nacimiento"])

            nuevo_usuario.save()

            return render(request, "usuario.html")

    else:
        nuevo_formulario_usuario = formulario_usuario_ingresado()

    formulario_de_ingreso = formulario_usuario_ingresado()

    return render(request, "Login_usuario.html", {"formulario":formulario_de_ingreso})


def ver_usuario_ingresado(request):


    return render(request, "usuario.html")


