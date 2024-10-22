from django.db import models

class Fabricante(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    fabricante = models.ForeignKey(Fabricante, on_delete=models.CASCADE, related_name='productos')

    def __str__(self):
        return self.nombre
