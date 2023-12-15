from django.urls import path
from inventario.views import listarProductos,crearProducto,eliminarProducto,editarProducto

urlpatterns = [
    path('',listarProductos,name='listado'),
    path('crear/',crearProducto,name='crear'),
    path('eliminar/<id>',eliminarProducto,name='eliminar'),
    path('editar/<id>',editarProducto,name='editar')
]