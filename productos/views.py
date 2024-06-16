from django.shortcuts import render, get_object_or_404
from .models import Producto
from categorias.models import Categoria
# Create your views here.


def productos(request, categoria_slug=None):
    categorias = None
    prod = None

    if categoria_slug != None:
        categorias = get_object_or_404(Categoria, slug=categoria_slug)
        prod = Producto.objects.filter(categoria=categorias, habilitado=True)
        cant_producto = prod.count()
    else:
        prod = Producto.objects.all().filter(habilitado=True)
        cant_producto = prod.count()

    context = {
        'prod': prod,
        'cant_producto': cant_producto,
    }
    return render(request,'tienda/productos.html', context)

def detalle_producto(request, categoria_slug, producto_slug):
    try:
        producto_unico = Producto.objects.get(categoria__slug=categoria_slug, slug=producto_slug)
    except Exception as e:
        raise e

    context = {
        'producto_unico': producto_unico,
    }
    return render(request, 'tienda/detalle_producto.html', context)