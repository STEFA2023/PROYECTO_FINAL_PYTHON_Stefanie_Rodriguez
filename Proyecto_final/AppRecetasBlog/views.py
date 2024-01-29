from django.shortcuts import render
from AppRecetasBlog.models import recetas_ingresadas
from AppRecetasBlog.forms import recetas_ingresadas_formulario
from AppRecetasBlog.models import usuario_ingresado
from AppRecetasBlog.forms import formulario_usuario_ingresado
from AppRecetasBlog.models import ingreso_al_blog
from AppRecetasBlog.forms import formulario_ingreso_al_blog
from AppRecetasBlog.models import info_de_contacto
from AppRecetasBlog.forms import formulario_de_contacto
from django.utils import timezone
# Create your views here.

#views Inicio

def inicio(request):
    return render(request, 'index.html')


#CRUD recetas:


#Views Crear de recetas

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

    formulario_de_ingreso_recetas = recetas_ingresadas_formulario()

    return render(request, "creador_de_recetas.html", {"formulario":formulario_de_ingreso_recetas})

# Views Ver recetas en la base de datos: 

def ver_recetas_ingresadas(request):

    recetas = recetas_ingresadas.objects.all()
    return render(request, "recetas.html", {'recetas_ingresadas': recetas})


#Views Editar recetas:

def editar_receta(request, receta_id):
    receta = get_object_or_404(recetas_ingresadas, pk=receta_id)

    if request.method == "POST":
        formulario_recetas = recetas_ingresadas_formulario(request.POST, instance=receta)
        if formulario_recetas.is_valid():
            formulario_recetas.save()
            return redirect('ver_recetas_ingresadas')

    else:
        formulario_recetas = recetas_ingresadas_formulario(instance=receta)

    return render(request, "editar_receta.html", {"formulario": formulario_recetas})

# Views Eliminar recetas:

def eliminar_receta(request, receta_id):
    receta = get_object_or_404(recetas_ingresadas, pk=receta_id)
    receta.delete()
    return redirect('ver_recetas_ingresadas')



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

    formulario_de_ingreso_usuario= formulario_usuario_ingresado()

    return render(request, "Login_usuario.html", {"formulario":formulario_de_ingreso_usuario})


def ver_usuario_ingresado(request):


    return render(request, "usuario.html")


# Views Ingreso de historias al blog

def agregar_blog(request):

    if request.method=="POST":

        info_ingreso_al_blog = formulario_ingreso_al_blog(request.POST)
        if info_ingreso_al_blog.is_valid():

            info = info_ingreso_al_blog.cleaned_data

            nuevo_blog = ingreso_al_blog(titulo=info["titulo"], tema=info["tema"], historia=info["historia"], fecha = timezone.now())

            nuevo_blog.save()

            return render(request, "blog.html")

    else:
        nuevo_formulario_blog = formulario_ingreso_al_blog()

    formulario_de_ingreso_blog = formulario_ingreso_al_blog()

    return render(request, "ingreso_al_blog.html", {"formulario":formulario_de_ingreso_blog})

#blogs en la base de datos:

def ver_blog_ingresado(request):

    entradas_blog = ingreso_al_blog.objects.all()

    return render(request, "blog.html", {'entradas_blog': entradas_blog})

#views Sobre mi:

def sobre_mi(request):
    return render(request, 'sobre_mi.html')


#views Contacto:

def contacto(request):
    formulario = formulario_de_contacto()
    return render(request, 'contacto.html', {'formulario_de_contacto': formulario})
