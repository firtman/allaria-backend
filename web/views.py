from django.shortcuts import render
from django.http import HttpResponse
from .models import Categoria, Producto

# Create your views here. Controlador del MVC, Vista del MTV
def index(request):
    # return HttpResponse("<h1>Hola</h1>", content_type="text/html")
    return render(request, "index.html", {
        "cantidad": Categoria.objects.count(),
        "categorias": Categoria.objects.all().order_by("nombre")
    })
