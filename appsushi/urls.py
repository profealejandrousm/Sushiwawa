from django.urls import path
from django.urls import include, path
from .views import index, menu, miscompras, productos

urlpatterns = [
    path('',index,name='index'),
    path('menu/',menu, name='menu'),
    path('miscompras/', miscompras, name='miscompras' ),
    path('productos/',productos, name='productos'),
]