from django.db import models

# Create your models here.
class recetas_ingresadas(models.Model):
    nombre = models.CharField(max_length = 50)
    autor = models.CharField(max_length = 20)
    ingrediente_principal = models.CharField(max_length = 100)
    procedimiento = models.CharField(max_length = 2000)
    cantidad_de_comensales = models.DateField(max_length = 10)