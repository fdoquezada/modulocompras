from turtle import update
from django.db import models

# Create your models here.

class Cliente(models.Model):
    rut = models.CharField(max_length=20, null=True, blank=True)
    nombres = models.CharField(max_length=200, null=True, blank=True)
    apellidos= models.CharField(max_length=200, null=True, blank=True)
    telefono = models.CharField(max_length=15, null=True, blank=True)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'clientes'
        verbose_name_plural = 'clientes'
        
    def __str__(self):
        return self.nombres  
    

class Producto(models.Model):
    codigo = models.CharField(max_length=255, unique=True, null=True, blank=True) 
    descripcion = models.CharField(max_length=255, unique=True, null=False)
    imagen = models.ImageField(upload_to='productos', null=True, blank=True)
    costo = models.DecimalField(max_digits=15, decimal_places=2, null=False)
    cantidad = models.DecimalField(max_digits=15, decimal_places=2, null=False)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'producto'
        verbose_name_plural = 'productos'
        order_with_respect_to = 'descripcion'
        
    def __str__(self):
        return self.descripcion 