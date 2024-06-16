from django.shortcuts import render
from productos.models import Producto

def home(request):
    productos = Producto.objects.all().filter(habilitado=True)

    context = {
        'productos': productos,
    }
    return render(request, 'home.html', context)
