from django.shortcuts import render, redirect
from .models import Producto
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Utilizando django rest framework, puedo agregar endpoints como en flask
from rest_framework.generics import GenericAPIView
from .serializers import ProductoSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


# Vamos a crear nuestra pagina inicial
def mostrarProductosPlantilla(request):
    # request > toda la información desde el navegador
    print(request)
    # data = [{
    #     'id': 1,
    #     'nombre': 'Lapiz Faber Castell',
    #     'descripcion': 'Lapiz B2'
    # },
    # {
    #     'id': 2,
    #     'nombre': 'Resaltador color amarillo',
    #     'descripcion': None
    # }]
    data = Producto.objects.all()
    # Podemos retornar un HTML para cuestiones que la aplicacion sea un monolito
    return render(request, 'mostrar_productos.html', {'data': data, 'mensaje': 'Bienvenido!'})

def crearProductosFormulario(request):
    if request.method == 'POST':
        # Para recibir la informacion prveniente del formulario, en base a sus names, usamos el request.post
        # print(request.POST.get('descripcionProducto'))
        # print(request.POST)
        nombreProducto = request.POST.get('nombreProducto')
        descripcionProducto = request.POST.get('descripcionProducto')
        # Inicializo mi nuevo registro del producto
        nuevoProducto = Producto(nombre = nombreProducto, descripcion = descripcionProducto)
        
        # Guarda el registro en la BD
        nuevoProducto.save()

        # como en teoria ya se agrego mi producto en la BD, entonces mandare un 
        # redireccionamiento a la vista de listar los productos
        return redirect('mostrar_productos')
    elif request.method == 'GET':
         return render(request, 'formulario_producto.html')
    
@api_view(http_method_names=['GET', 'POST'])
def validarFuncionamiento(request):
    # Este request que nos llega usando rest_framework es un request diferente a la de las plantillas
    # porq se usa de la libreria
    # https://www.django-rest-framework.org/api-guide/requests/
    if request.method == 'GET':
        # En DRF no se puede retornar una plantilla, sino que se tiene q retornar una respuesta HHTP, y
        # para q se pueda utilizar la clase Response
        return Response(data={
            'message': 'El servidor funciona exitosamente'
        })
    elif request.method == 'POST':
        # POara leer la informacion proveniente del body usamos el request.data
        print(request.data)
        return Response(data={
            'message': 'Informacion aceptada correctamente'
        })

# Al usar GenericAPIView esto es muy similar a como lo haciamos en flask, usando la clase Resource
class ProductosController(GenericAPIView):
    def get(self, request):
        # Select * from productos
        productos = Producto.objects.all()
        serializador = ProductoSerializer(productos, many=True)

        serializador.data

        return Response(data={
            'message': 'Los Productos son:',
            'content': serializador.data
        })
    def post(self, request):
        # la data proviene del request
        data = request.data
        serializador = ProductoSerializer(data=data)
        # Ahora como queremos validar si esta indormacion proveniente del cliente, es válida, usamos el metodo is_valid()
        if serializador.is_valid():
            # USando model serializer es muy facil guardar la informacion en la BD
            # aca la data ya es valida para guardarse
            serializador.save()
            return Response(data={
                'message': 'Producto creado exitosamente'
            })
        else:
            # si no es valida
            # si la informacion no es valida, los campos del porque no lo es, se guardaran en el atributo errors
            return Response(data={
                'message': 'Error al crear el producto',
                'content': serializador. errors
            })
        
class ListarYCrearProductosController(ListCreateAPIView):
    # Para utilizar una vista generica se tiene q definir los siguientes atributos
    # Como obtendra la informacion y la devolverá
    queryset = Producto.objects
    # Para indicar como se tiene q validar y devolver la informacion proveniente de la BD
    serializer_class = ProductoSerializer

class DevolverActualizarEliminarProductoController(RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects
    serializer_class = ProductoSerializer
    # Si cambiamos el nombre del parametro en nuestra url
    lookup_field = 'id'