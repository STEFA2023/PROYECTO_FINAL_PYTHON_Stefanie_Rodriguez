"""
URL configuration for Proyecto_final project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import Proyecto_final.views
from AppRecetasBlog.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', inicio, name= "Inicio"),
    path('crear_recetas/',agregar_receta, name="Agregar_Receta"),
    path('recetas/', ver_recetas_ingresadas, name="Ver_Recetas_Ingresadas"),
    path('Login_usuario/', agregar_usuario, name="Agregar_Usuario"),
    path('usuario/', ver_usuario_ingresado, name="Ver_Usuario_Ingresado"),
    path('ingreso_al_blog/', agregar_blog, name="Agregar_Blog"),
    path('blog/', ver_blog_ingresado, name="Ver_Blog_Ingresado"),
    path('sobre_mi/', sobre_mi, name="Sobre_Mi"),
]

