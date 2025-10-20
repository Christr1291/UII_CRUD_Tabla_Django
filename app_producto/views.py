# app_producto/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto # Importamos el modelo Producto

# Listar productos
def index(request):
    # Obtiene todos los productos de la base de datos
    productos = Producto.objects.all()
    # Renderiza la plantilla 'listar_productos.html' y le pasa la lista de productos
    return render(request, 'listar_productos.html', {'productos': productos})

# Ver producto (si necesitas una vista de detalle individual)
def ver_producto(request, id):
    # Busca un producto por su ID o devuelve un error 404 si no lo encuentra
    producto = get_object_or_404(Producto, id=id)
    # Renderiza la plantilla 'ver_producto.html' y le pasa el producto encontrado
    return render(request, 'ver_producto.html', {'producto': producto})

# Agregar producto
def agregar_producto(request):
    if request.method == 'POST':
        # Si la solicitud es POST, significa que el formulario ha sido enviado
        # Recoge los datos del formulario usando los nombres de campo correctos (nombre, descripcion, precio, stock)
        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']
        precio = request.POST['precio']
        stock = request.POST['stock']
        
        # Crea una nueva instancia de Producto con los datos recibidos
        Producto.objects.create(
            nombre=nombre,
            descripcion=descripcion,
            precio=precio,
            stock=stock
        )
        # Redirige al usuario a la página de inicio (listado de productos)
        return redirect('inicio')
    # Si la solicitud no es POST (es GET), simplemente muestra el formulario vacío
    return render(request, 'agregar_producto.html')

# Editar producto
def editar_producto(request, id):
    # Busca el producto por su ID para editarlo
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        # Si la solicitud es POST, actualiza los campos del producto con los datos del formulario
        producto.nombre = request.POST['nombre']
        producto.descripcion = request.POST['descripcion']
        producto.precio = request.POST['precio']
        producto.stock = request.POST['stock']
        producto.save() # Guarda los cambios en la base de datos
        # Redirige al usuario a la página de inicio
        return redirect('inicio')
    # Si la solicitud es GET, muestra el formulario de edición con los datos actuales del producto
    return render(request, 'editar_producto.html', {'producto': producto})

# Borrar producto
def borrar_producto(request, id):
    # Busca el producto por su ID para borrarlo
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        # Si la solicitud es POST (el usuario ha confirmado el borrado), elimina el producto
        producto.delete()
        # Redirige al usuario a la página de inicio
        return redirect('inicio')
    # Si la solicitud es GET, muestra la página de confirmación de borrado
    return render(request, 'borrar_productos.html', {'producto': producto})