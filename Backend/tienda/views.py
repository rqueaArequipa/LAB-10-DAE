from django.shortcuts import render, get_object_or_404
from .models import Categoria, Producto


def Index(request):
    product_list = Producto.objects.order_by('nombre')
    category_list = Categoria.objects.all()
    destacado = Producto.objects.get(nombre = 'Coca Cola 500ml')
    product_dest = Producto.objects.exclude(nombre=destacado)
    context = {
        'product_list': product_list,
        'category_list': category_list,
        'destacado': destacado,
        'product_dest': product_dest
    }
    return render(request, 'index.html', context)


def Product(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    category_list = Categoria.objects.all()
    context = {
        'producto': producto,
        'category_list': category_list,
    }
    return render(request, 'producto.html', context)

def Category(request, category_id):
    category = get_object_or_404(Categoria, pk=category_id)
    product_list = Producto.objects.filter(categoria=category)
    category_list = Categoria.objects.all()
    destacado = Producto.objects.get(nombre = 'Coca Cola 500ml')
    product_dest = Producto.objects.filter(categoria=category)
    if category_id == 1:
        destacado = Producto.objects.get(nombre = 'Fanta 500ml')
        product_dest = Producto.objects.exclude(nombre=destacado).filter(categoria=category)
    elif category_id == 2:
        destacado = Producto.objects.get(nombre = 'Cheetos')
        product_dest = Producto.objects.exclude(nombre=destacado).filter(categoria=category)
    elif category_id == 3:
        destacado = Producto.objects.get(nombre = 'Picaras')
        product_dest = Producto.objects.exclude(nombre=destacado).filter(categoria=category)
    elif category_id == 4:
        destacado = Producto.objects.get(nombre = 'Sublime')
        product_dest = Producto.objects.exclude(nombre=destacado).filter(categoria=category)
    context = {
        'product_list': product_list,
        'category_list': category_list,
        'destacado': destacado,
        'product_dest': product_dest
    }
    return render(request, 'category.html', context)
