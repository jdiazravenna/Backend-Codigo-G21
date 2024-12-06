from flask_restful import Resource, request
from models import ProductoModel
from marshmallow.exceptions import ValidationError
from .serializers import ProductoSerializer
from instancias import conexion

class ProductosController(Resource):
    def post(self):
        data=request.get_json()
        serializador = ProductoSerializer()
        try:
            data_validada = serializador.load(data)
            nuevo_producto = ProductoModel(**data_validada)

            conexion.session.add(nuevo_producto)
            conexion.session.commit()

            resultado = serializador.dump(nuevo_producto)
            return {
                'content': resultado,
                'message': 'Producto creado exitosamente'
            }
            
        except ValidationError as error:
            return {
                'message': 'Error al crear producto',
                'content': error.args
            }