from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'appsushi/index.html')


def productos(request):
    return render(request,'appsushi/productos.html')

def miscompras(request):
    return render(request,'appsushi/miscompras.html')