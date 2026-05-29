from django.db import models

# Create your models here.
class Producto(models.Model):
    id=models.IntegerField(primary_key=True, null=False)
    nombre_producto=models.CharField(max_length=50, null=False)
    descripcion=models.CharField(max_length=250, null=False)
    precio=models.IntegerField(null=False)
    
    
    def __str__(self):
        return self.nombre_producto