from flask_restful import Resource, request
from models import CategoriaModel
from instancias import conexion
from .serializers import CategoriaSerializer
from marshmallow.exceptions import ValidationError

# Al heredar la clase Resource, ahora los metodos de la clase, 
# tendran q tener el nombre d elos metodos http, para q swean llamados correctamente
class CategoriaController(Resource):
    def get(self):
        # Select * From categorias;
        data = conexion.session.query(CategoriaModel).all()
        # Convertir esta informacion de instancias, a un diccionario, para devolverlo usando marshmallow
        serializador = CategoriaSerializer()
        resultado = serializador.dump(data , many=True)
        return {
            'message': 'Las categorías son',
            'result': resultado
        }
    def post(self):
        # Obtenemos la informacion del body proveniente del request
        data = request.get_json()
        serializador = CategoriaSerializer()
        try:
            # Carga la informacion y validara con el serializador, si falla, emitira un error
            data_serializada = serializador.load(data)

            # cargo la informacion serializada a la nueva instancia de la categoria

            # Cuando yo quiero pasar un diccionario a parametros de una clase o funcion,
            #  con los mismos nosmbres de los parametros que las llaves del diccionario
            # data_serializada= {'nombre':'xyz', 'fechaCreacion':'2022-12-01'}
            # CategoriaModel(nombre='xyz', fechaCreacion='2022-12-01')
            nueva_categoria = CategoriaModel(**data_serializada)

            # Agregamos el nuevo registro a nuestra BD
            conexion.session.add(nueva_categoria)

            # indicamos q los cambios deben guardarse de manera permanente (usando una transaccion)
            conexion.session.commit()

            resultado = serializador.dump(nueva_categoria)
            return {
                'message': 'Categoría creada exitosamente',
                'content': resultado
            }
        except ValidationError as error:
            return {
                'message': 'Error al crea la categoria',
                'content': error.args # muestra la descripcion del error              
            }
            