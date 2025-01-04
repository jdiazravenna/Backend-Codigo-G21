from django.urls import path
from .views import (mostrarProductosPlantilla, crearProductosFormulario)

# para definir las rutas que van a comportarse en esta aplicacion, usamos la variable urlpatterns
urlpatterns = [
    path('mostrar-productos', mostrarProductosPlantilla, name='mostrar_productos'),
    path('crear-producto', crearProductosFormulario, name='crear_producto')
]