# En mywebapp/views.py

from django.shortcuts import render, redirect
from .models import Categoria, Producto, Cliente
from .forms import CategoriaForm, ProductoForm, ClienteForm
from .forms import SearchForm


def index(request):
    categorias = Categoria.objects.all()
    productos = Producto.objects.all()
    clientes = Cliente.objects.all()
    return render(request, 'index.html', {'categorias': categorias, 'productos': productos, 'clientes': clientes})

def add_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CategoriaForm()
    return render(request, 'add_categoria.html', {'form': form})


def add_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProductoForm()
    return render(request, 'add_producto.html', {'form': form})


def add_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ClienteForm()
    return render(request, 'add_cliente.html', {'form': form})


def search_categorias(request):
    form = SearchForm(request.GET)
    query = request.GET.get('query', '')
    
    categorias = Categoria.objects.filter(nombre__icontains=query)
    
    return render(request, 'search_results.html', {'form': form, 'resultados': categorias, 'query': query})

def search_productos(request):
    form = SearchForm(request.GET)
    query = request.GET.get('query', '')
    
    productos = Producto.objects.filter(nombre__icontains=query)
    
    return render(request, 'search_results.html', {'form': form, 'resultados': productos, 'query': query})

def search_clientes(request):
    form = SearchForm(request.GET)
    query = request.GET.get('query', '')
    
    clientes = Cliente.objects.filter(nombre__icontains=query) | Cliente.objects.filter(direccion__icontains=query)
    
    return render(request, 'search_results.html', {'form': form, 'resultados': clientes, 'query': query})
