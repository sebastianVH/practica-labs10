from django.db import models

# Create your models here.
'''
Crearemos el modelo Productos con los campos de nombre, precio y stock
'''
class Productos(models.Model):
    #creamos los campos
    nombre = models.CharField(max_length=30)
    precio = models.FloatField()
    stock = models.IntegerField(max_length=5)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
    
    
