from django.shortcuts import render
from django.http import JsonResponse
from web.models import Categoria, Producto

# Create your views here.
def get_categorias(request):
    categorias = Categoria.objects.all().values()
    lista_categorias = list(categorias)
    # return JsonResponse({
    #     "ok": True,
    #     "categorias": lista_categorias
    # }, safe=False)
    response = JsonResponse(lista_categorias, safe=False)
    response['Access-Control-Allow-Origin'] = "*"
    return response

def get_productos(request):
    productos = Producto.objects.all().values()
    lista_productos = list(productos)
    response = JsonResponse(lista_productos, safe=False) 
    response['Access-Control-Allow-Origin'] = "*"
    return response
