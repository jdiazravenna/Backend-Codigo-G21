from django.urls import path
from .views import (mostrarProductosPlantilla, 
                    crearProductosFormulario,
                    validarFuncionamiento,
                    ProductosController,
                    ListarYCrearProductosController,
                    DevolverActualizarEliminarProductoController)



# para definir las rutas que van a comportarse en esta aplicacion, usamos la variable urlpatterns
urlpatterns = [
    path('mostrar-productos', mostrarProductosPlantilla, name='mostrar_productos'),
    path('crear-producto', crearProductosFormulario, name='crear_producto'),
    # Al usar una funcion que sea de django rest framework DRF
    # No se recomienda definir un name porque no se hará un redireccionamiento hacia esta ruta
    path('validar-funcionamiento', validarFuncionamiento),
    # Al momento de usar una clase DRF django rest framework, tenemos que indicar que vamos a convertirla a una vista
    # para que pueda enterderla django
    path('productos', ProductosController.as_view()),
    path('productos-v2', ListarYCrearProductosController.as_view()),
    # Cuando usamos alguna de las vistas genericas que devuelvan, actualicen o eliminen un registro, en la ruta tenemos q agregar el id
    # Solamente aceptara el id, si colocamos otro nombre, lanzara un error y por ende no podremos realizar la accion
    # Si queremos cambiar el nombre, debemos establecerlo en el atributo lookup_field
    path('producto/<id>', DevolverActualizarEliminarProductoController.as_view())
]