from django.shortcuts import redirect, render
from datetime import date
from .models import Producto
from .forms import ProductoForm

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

def productos(request):
    listaproductos=Producto.objects.all()
    total=listaproductos.count()
    
    context={
         "productos":listaproductos,
         "total":total
    }
    return render(request,'appsushi/productos.html', context)

def crearproducto(request):
    form=ProductoForm()
    
    if request.method == "POST":
        form=ProductoForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("productos")
            
        else:
            context["form":form]
 
    
    context={
        "form":form,
       
    }
    return render(request,"appsushi/crearproducto.html", context)