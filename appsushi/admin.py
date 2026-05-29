from django.contrib import admin
from .models import Producto
# Register your models here.

class AdmProducto(admin.ModelAdmin):
    list_display=['nombre_producto','descripcion','precio']
    search_fields=['nombre_producto','precio']
    list_filter=['nombre_producto','precio']
    
    
admin.site.register(Producto,AdmProducto)
