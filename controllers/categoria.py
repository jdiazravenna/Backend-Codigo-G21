from flask_restful import Resource, request
from instancias import conexion
from models import Categoria
from .serializers import CategoriaSerializer
from marshmallow.exceptions import ValidationError
from flask_jwt_extended import jwt_required

class CategoriaController(Resource):
    # Atributo de la clase
    serializador = CategoriaSerializer()
    
    @jwt_required()
    def post(self):
        data = request.get_json()
        try:
            data_serializada = self.serializador.load(data)
            # { 'nombre': 'ejemplo', 'color': 'azul' }
            # 'nombre' = 'ejemplo', 'color' = 'azul'
            nueva_categoria = Categoria(**data_serializada)
            conexion.session.add(nueva_categoria)
            conexion.session.commit()

            resultado = self.serializador.dump(nueva_categoria)
            return {
                'message': 'Categoria creada exitosamente',
                'content': resultado
            }

        except ValidationError as error:
            return {
                'message': 'Error al crear la categoria',
                'content': error.args
            }
    def get(self):
        # Select * from categorias;
        categorias = conexion.session.query(Categoria).all()

        return {
            'content': self.serializador.dump(categorias, many=True)
        }