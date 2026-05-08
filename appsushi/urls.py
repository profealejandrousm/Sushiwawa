from django.urls import path
from django.urls import include, path
from .views import index, productos

urlpatterns = [
    path('',index,name='index'),
    path('productos/',productos, name='productos')
]