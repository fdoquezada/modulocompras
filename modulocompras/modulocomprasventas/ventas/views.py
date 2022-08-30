from multiprocessing import context
from django.shortcuts import render, redirect
from .models import Cliente, Producto

# Create your views here.

def ventas_view(request):
    return render(request,'ventas.html')

def clientes_view(request):
    Clientes = Cliente.objects.all()
    context = {
        'clientes': Clientes,
        
    }
    return render(request, 'clientes.html', context)


def add_cliente_view(request):

    return render(request, 'clientes.html', context)


def edit_cliente_view(request):

    return render(request, 'clientes.html', context)


def delete_cliente_view(request):

    return render(request, 'clientes.html', context)