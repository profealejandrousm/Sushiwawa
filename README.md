# Tutorial Django: Registrar y listar productos con SQLite

Este tutorial muestra los pasos para crear un modelo de `Producto` en Django con los campos:

- nombre
- imagen
- descripcion
- valor

Además, se explica cómo registrar productos desde un formulario y listarlos desde una base de datos SQLite.

La estructura base del proyecto es la siguiente:

```text
proyecto/
│
├── manage.py
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
└── app/
    ├── models.py
    ├── views.py
    ├── urls.py
    ├── forms.py
    └── templates/
```

---

## 1. Verificar que la app esté registrada

Abre el archivo:

```text
config/settings.py
```

Busca la sección `INSTALLED_APPS` y agrega tu aplicación:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'app',
]
```

---

## 2. Verificar configuración de SQLite

En el mismo archivo `config/settings.py`, revisa que tengas algo como esto:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

Django normalmente ya trae SQLite configurado por defecto, por lo tanto no necesitas instalar MySQL ni PostgreSQL para este ejemplo.

---

## 3. Configurar carga de imágenes

Como el producto tendrá una imagen, debemos configurar los archivos multimedia.

En `config/settings.py`, agrega al final:

```python
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

Esto permitirá que las imágenes subidas se guarden en una carpeta llamada `media`.

La estructura quedará así después de subir imágenes:

```text
proyecto/
├── media/
│   └── productos/
│       └── imagen_producto.jpg
```

---

## 4. Instalar Pillow

Para usar `ImageField`, Django necesita la librería Pillow.

Ejecuta en la terminal, dentro de tu entorno virtual:

```bash
pip install pillow
```

---

## 5. Crear el modelo Producto

Abre el archivo:

```text
app/models.py
```

Agrega el siguiente código:

```python
from django.db import models


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='productos/')
    descripcion = models.TextField()
    valor = models.IntegerField()

    def __str__(self):
        return self.nombre
```

Explicación rápida:

```python
nombre = models.CharField(max_length=100)
```

Guarda el nombre del producto.

```python
imagen = models.ImageField(upload_to='productos/')
```

Guarda la imagen dentro de:

```text
media/productos/
```

```python
descripcion = models.TextField()
```

Permite guardar una descripción más extensa.

```python
valor = models.IntegerField()
```

Guarda el precio o valor como número entero.

---

## 6. Crear las migraciones

Cada vez que creas o modificas un modelo, debes generar y aplicar migraciones.

Desde la carpeta donde está `manage.py`, ejecuta:

```bash
python manage.py makemigrations
```

Luego ejecuta:

```bash
python manage.py migrate
```

Esto creará la tabla del producto en SQLite.

---

## 7. Registrar el modelo en el administrador

Abre el archivo:

```text
app/admin.py
```

Agrega:

```python
from django.contrib import admin
from .models import Producto


admin.site.register(Producto)
```

Ahora puedes administrar productos desde el panel de Django.

Crea un superusuario:

```bash
python manage.py createsuperuser
```

Luego ejecuta el servidor:

```bash
python manage.py runserver
```

Entra a:

```text
http://127.0.0.1:8000/admin/
```

---

## 8. Crear un formulario para Producto

Crea el archivo:

```text
app/forms.py
```

Agrega:

```python
from django import forms
from .models import Producto


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'imagen', 'descripcion', 'valor']
```

Este formulario se basa directamente en el modelo `Producto`.

---

## 9. Crear las vistas para registrar y listar productos

Abre el archivo:

```text
app/views.py
```

Agrega:

```python
from django.shortcuts import render, redirect
from .models import Producto
from .forms import ProductoForm


def registrar_producto(request):
    if request.method == 'POST':
        formulario = ProductoForm(request.POST, request.FILES)

        if formulario.is_valid():
            formulario.save()
            return redirect('listar_productos')
    else:
        formulario = ProductoForm()

    return render(request, 'app/registrar_producto.html', {
        'formulario': formulario
    })


def listar_productos(request):
    productos = Producto.objects.all()

    return render(request, 'app/listar_productos.html', {
        'productos': productos
    })
```

Punto importante:

```python
request.FILES
```

Es necesario porque el formulario subirá imágenes.

---

## 10. Crear las rutas de la app

Crea el archivo:

```text
app/urls.py
```

Agrega:

```python
from django.urls import path
from . import views


urlpatterns = [
    path('', views.listar_productos, name='listar_productos'),
    path('registrar/', views.registrar_producto, name='registrar_producto'),
]
```

Con esto tendrás dos rutas:

```text
/
```

Lista los productos.

```text
/registrar/
```

Permite registrar un producto.

---

## 11. Conectar las rutas de la app con el proyecto

Abre el archivo:

```text
config/urls.py
```

Déjalo así:

```python
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

La parte final es muy importante:

```python
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

Esto permite mostrar las imágenes mientras estás trabajando en desarrollo.

---

## 12. Crear las carpetas de templates

Dentro de `app`, crea esta estructura:

```text
app/
└── templates/
    └── app/
        ├── registrar_producto.html
        └── listar_productos.html
```

La estructura completa se verá así:

```text
proyecto/
├── manage.py
├── config/
│   ├── settings.py
│   └── urls.py
│
└── app/
    ├── models.py
    ├── views.py
    ├── urls.py
    ├── forms.py
    └── templates/
        └── app/
            ├── registrar_producto.html
            └── listar_productos.html
```

---

## 13. Crear template para registrar producto

Crea el archivo:

```text
app/templates/app/registrar_producto.html
```

Agrega:

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Registrar Producto</title>
</head>
<body>

    <h1>Registrar producto</h1>

    <form method="POST" enctype="multipart/form-data">
        {% csrf_token %}

        {{ formulario.as_p }}

        <button type="submit">Guardar producto</button>
    </form>

    <br>

    <a href="{% url 'listar_productos' %}">Ver productos</a>

</body>
</html>
```

Punto importante:

```html
enctype="multipart/form-data"
```

Es obligatorio cuando el formulario permite subir archivos o imágenes.

---

## 14. Crear template para listar productos

Crea el archivo:

```text
app/templates/app/listar_productos.html
```

Agrega:

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Listado de Productos</title>
</head>
<body>

    <h1>Listado de productos</h1>

    <a href="{% url 'registrar_producto' %}">Registrar nuevo producto</a>

    <hr>

    {% for producto in productos %}

        <div>
            <h2>{{ producto.nombre }}</h2>

            {% if producto.imagen %}
                <img src="{{ producto.imagen.url }}" alt="{{ producto.nombre }}" width="200">
            {% endif %}

            <p>{{ producto.descripcion }}</p>

            <p>
                <strong>Valor:</strong> ${{ producto.valor }}
            </p>
        </div>

        <hr>

    {% empty %}

        <p>No existen productos registrados.</p>

    {% endfor %}

</body>
</html>
```

---

## 15. Ejecutar el servidor

Desde la carpeta donde está `manage.py`, ejecuta:

```bash
python manage.py runserver
```

Luego entra a:

```text
http://127.0.0.1:8000/
```

Ahí deberías ver el listado de productos.

Para registrar uno nuevo, entra a:

```text
http://127.0.0.1:8000/registrar/
```

---

## 16. Resumen de archivos modificados

### `app/models.py`

```python
from django.db import models


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='productos/')
    descripcion = models.TextField()
    valor = models.IntegerField()

    def __str__(self):
        return self.nombre
```

---

### `app/forms.py`

```python
from django import forms
from .models import Producto


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'imagen', 'descripcion', 'valor']
```

---

### `app/views.py`

```python
from django.shortcuts import render, redirect
from .models import Producto
from .forms import ProductoForm


def registrar_producto(request):
    if request.method == 'POST':
        formulario = ProductoForm(request.POST, request.FILES)

        if formulario.is_valid():
            formulario.save()
            return redirect('listar_productos')
    else:
        formulario = ProductoForm()

    return render(request, 'app/registrar_producto.html', {
        'formulario': formulario
    })


def listar_productos(request):
    productos = Producto.objects.all()

    return render(request, 'app/listar_productos.html', {
        'productos': productos
    })
```

---

### `app/urls.py`

```python
from django.urls import path
from . import views


urlpatterns = [
    path('', views.listar_productos, name='listar_productos'),
    path('registrar/', views.registrar_producto, name='registrar_producto'),
]
```

---

### `config/urls.py`

```python
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

---

### `config/settings.py`

Agregar la app:

```python
INSTALLED_APPS = [
    # apps de Django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # app propia
    'app',
]
```

Agregar al final:

```python
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

---

## 17. Posibles errores comunes

### Error 1: No se muestra la imagen

Revisa que en `config/urls.py` tengas:

```python
from django.conf import settings
from django.conf.urls.static import static
```

Y al final:

```python
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

---

### Error 2: El formulario no sube imágenes

Revisa que el formulario HTML tenga:

```html
enctype="multipart/form-data"
```

Y que la vista use:

```python
request.FILES
```

Ejemplo:

```python
formulario = ProductoForm(request.POST, request.FILES)
```

---

### Error 3: Django no reconoce ImageField

Instala Pillow:

```bash
pip install pillow
```

---

### Error 4: La tabla no existe en SQLite

Ejecuta nuevamente:

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## Resultado esperado

Con este tutorial ya tienes un CRUD inicial, al menos con registro y listado de productos usando:

- Django
- SQLite
- Formularios basados en modelos
- Subida de imágenes
- Templates HTML
- Rutas internas de aplicación
