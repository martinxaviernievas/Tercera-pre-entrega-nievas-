from django.urls import path
from .views import index, add_categoria, add_producto, add_cliente
from .views import search_categorias, search_productos, search_clientes


urlpatterns = [
    path('', index, name='index'),
    path('add_categoria/', add_categoria, name='add_categoria'),
    path('add_producto/', add_producto, name='add_producto'),
    path('add_cliente/', add_cliente, name='add_cliente'),
    path('search_categorias/', search_categorias, name='search_categorias'),
    path('search_productos/', search_productos, name='search_productos'),
    path('search_clientes/', search_clientes, name='search_clientes'),

    # Agrega más URLs según tus necesidades
]