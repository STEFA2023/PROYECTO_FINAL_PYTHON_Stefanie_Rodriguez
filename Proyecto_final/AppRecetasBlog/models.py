from django.db import models

# Create your models here.

#models Ingreso de recetas

class recetas_ingresadas(models.Model):

    def __str__(self):
        return f"Nombre: {self.nombre} ------ Autor: {self.autor}"

    nombre = models.CharField(max_length = 50)
    autor = models.CharField(max_length = 20)
    ingrediente_principal = models.CharField(max_length = 100)
    ingredientes = models.TextField()
    procedimiento = models.CharField(max_length = 2000)
    cantidad_de_comensales = models.CharField(max_length = 10)


#models Ingreso de Usuario

class usuario_ingresado(models.Model):

    def __str__(self):
        return f"Nombre: {self.nombre} ------ Mail: {self.email}"
    
    nombre = models.CharField(max_length = 50)
    apellido = models.CharField(max_length = 50)
    edad = models.IntegerField()
    email = models.EmailField(default="")
    pais = models.CharField(max_length = 2000)
    fecha_de_nacimiento = models.DateField()


#models Ingreso blog libre
    
class ingreso_al_blog(models.Model):

    def __str__(self):
        return f"Titulo: {self.titulo} ------ Tema: {self.tema}"
    
    titulo = models.CharField(max_length=500)
    tema = models.CharField(max_length=1000)
    historia = models.CharField(max_length= 6000)


#models Contacto

class info_de_contacto(models.Model):

    def __str__(self):
        return f"Nombre: {self.Nombre_Completo} ------ Email: {self.email}"
    
    Nombre_Completo = models.CharField(max_length= 100)
    email = models.EmailField()
    consulta = models.CharField(max_length= 6000)