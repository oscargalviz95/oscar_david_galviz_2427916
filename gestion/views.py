from django.shortcuts import render

from .models import Producto, Categoria

def productos(request):
    data = {
        'productos': Producto.objects.all(),
    }
    return render(request, 'productos.html', data)

def categorias(request):
    data = {
        'categorias': Categoria.objects.all(),
    }
    return render(request, 'categorias.html', data)