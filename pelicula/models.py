from django.db import models

class Pelicula(models.Model):
    nombre = models.CharField(max_length=70, blank=False, default='')
    descripcion = models.CharField(max_length=200,blank=False, default='')
    categoria = models.CharField(max_length=70,blank=False, default='')
    genero = models.CharField(max_length=70,blank=False, default='')
    fecha=models.DateTimeField(blank=True, null=True)