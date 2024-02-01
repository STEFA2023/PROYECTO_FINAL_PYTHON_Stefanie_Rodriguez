from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import get_object_or_404, redirect
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

#Views Ingreso de Usuarios

def login_request(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():

            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username= usuario, password=contrasenia)

            if user is not None:
                login(request, user)

                return render(request, "../AppRecetasBlog/templates/index.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, "../AppRecetasBlog/templates/index.html", {"mensaje":"Datos incorrectos"})
        else:

            return render(request, "../AppRecetasBlog/templates/index.html", {"mensaje":"Formulario erroneo"})

    form = AuthenticationForm()

    return render(request, "login.html", {"form": form})

#views registro de usuario:

def register(request):

    if request.method == 'POST':

            form = UserCreationForm(request.POST)
            if form.is_valid():

                username = form.cleaned_data['username']
                form.save()
                return render(request,"../AppRecetasBlog/templates/index.html",  {"mensaje":"Usuario Creado :)"})

    else:       
            form = UserCreationForm()     

    return render(request,"registro_usuario.html" ,  {"form":form})


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
