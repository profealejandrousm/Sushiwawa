from django.shortcuts import render
from datetime import date
from .models import Producto

# Create your views here.
def index(request):
    return render(request,'appsushi/index.html')


def menu(request):
    productos=Producto.objects.all()
    
    context={
        "productos":productos
    }
    
    return render(request,'appsushi/menu.html', context)

def miscompras(request):
    fecha=date.today()
    nombre="Wacoldo"
    lista=["lunes","martes","miercoles","jueves","viernes"]
    
    context={
        "fecha":fecha,
        "nombre":nombre,
        "dias":lista
    }
    
    
    return render(request,'appsushi/miscompras.html', context)