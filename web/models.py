from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=40)
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    precio = models.FloatField()
    disponible = models.BooleanField(default=True)
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.nombre} ${self.precio} ({self.categoria.nombre})'
