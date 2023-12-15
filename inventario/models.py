from django.db import models

# Create your models here.
'''
Crearemos el modelo Productos con los campos de nombre, precio y stock
'''
class Categorias(models.Model):
    '''
    La clase Categorias va a ser una clave FORANEA que se usara en mis productos:
    Un producto, podra tener una categoria asociada, y una categoria puede tener VARIOS productos asociados
    '''
    nombre = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

class Productos(models.Model):
    #creamos los campos
    nombre = models.CharField(max_length=30)
    precio = models.FloatField()
    stock = models.IntegerField()
    categoria_fk = models.ForeignKey(Categorias,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
    
    
