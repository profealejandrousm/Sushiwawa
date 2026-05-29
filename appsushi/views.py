from django.shortcuts import render
from datetime import date

# Create your views here.
def index(request):
    return render(request,'appsushi/index.html')


def productos(request):
    return render(request,'appsushi/productos.html')

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