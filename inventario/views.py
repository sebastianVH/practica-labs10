from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from inventario.models import Productos,Categorias

# Create your views here.
def listarProductos(req):
    #buscar y almacenar la lista de Productos
    productos = Productos.objects.all()
    categorias = Categorias.objects.all()
    #contexto: es un diccionario en el cual la clave es el recurso HTML a usar, y el valor, el dato se enviara
    contexto = {'lista_productos': productos,'lista_categorias':categorias}
    #RENDERIZAR mi contexto:
    return render(req,'listado_productos.html',contexto)

def crearProducto(req):
    #tomamos los datos que vienen por POST 
    nombre_producto = req.POST["nombre"]
    precio_producto = req.POST["precio"]
    stock_producto = req.POST["stock"]
    categoria = req.POST['categoria']
    categoria_asociada = Categorias.objects.get(id=categoria)
    producto_creado = Productos(nombre=nombre_producto,precio=precio_producto,stock=stock_producto,categoria_fk=categoria_asociada) #objeto de un producto creado
    #una vez creada la INSTANCIA de un producto, debo ALMACENARLA
    producto_creado.save() #! SIEMPRE USAR EL SAVE!!! SINO NUESTRO OBJETO NO SE ALMACENARA
    return redirect('listado')
    
def eliminarProducto(req,id):
    producto_a_eliminar = get_object_or_404(Productos,id=id)
    producto_a_eliminar.delete()
    return redirect('listado')
    

def editarProducto(req,id):
    #2 metodos: GET y POST
    #GET: voy a BUSCAR Y LISTAR EL PRODUCTO
    producto_a_editar = get_object_or_404(Productos,id=id)
    categorias = Categorias.objects.all()
    if req.method == 'GET':
        contexto = {'producto':producto_a_editar,'categorias':categorias}
        return render(req,'editar_producto.html',contexto)
    elif req.method == 'POST':
        nombre_nuevo = req.POST["nombre"]
        precio_nuevo = req.POST["precio"]
        stock_nuevo = req.POST["stock"]
        categoria_nueva = req.POST['categoria']
        categoria_asociada_nueva = Categorias.objects.get(id=categoria_nueva)
        producto_a_editar.nombre = nombre_nuevo
        producto_a_editar.precio = precio_nuevo
        producto_a_editar.stock = stock_nuevo
        producto_a_editar.categoria_fk = categoria_asociada_nueva
        producto_a_editar.save()
        return redirect('listado')
        
    
    #POST: voy a ACTUALIZAR EL PRODUCTO