from django.db import models

class Categoria(models.Model):
     nombre = models.CharField(max_length=20)
     descripcion = models.TextField(max_length=30)
     
     def __str__(self):
         return self.nombre

class Producto(models.Model):
     producto = models.CharField(max_length=20)
     descripcion = models.TextField(max_length=30)
     precio = models.IntegerField()
     categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
     
     def __str__(self):
         return self.producto