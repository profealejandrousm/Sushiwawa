from django import forms
from .models import Producto
from django.contrib.auth.forms import UserCreationForm


class customUserCreationForm(UserCreationForm):
    pass



class ProductoForm(forms.ModelForm):
    
    nombre_producto=forms.CharField(max_length=100, required=True,error_messages={'required':"Debe agregar el nombre del producto"})
    descripcion=forms.CharField(max_length=250, required=True, error_messages={'required':"Agregue descripción"})
    precio=forms.IntegerField(initial=0, min_value=0, required=True, error_messages={'required':"El precios debe ser mayor o igual que cero"})
    imagen=forms.ImageField()
    
    class Meta:
        model = Producto
        fields = ['nombre_producto','descripcion','precio', 'imagen']
