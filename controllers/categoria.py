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
            
# Cuando queremos trabajar en otra ruta, o utlizar otra vez un metodo ya creado
# cuando ponemos en un metodo http un parametro, significa que vamos a recibir ese parametro por la URL
class ManejoCategoriaController(Resource):
    def validarCategoria(self, id):
        # filter > hace la comparacion entre los atributos de la clase
        # filter_by > hace la comparacion entre parametros, mas no utiliza atributos
        # el filter es mejor porque nos permite hacer busquedas mas avanzadas como  like, ilike, mayor que, menor que, etc

        # Select * from categorias where id  '...' limit 1;
        categoria_encontrada = conexion.session.query(CategoriaModel).filter(
            CategoriaModel.id == int(id)).first()
        # Opeador terneareo
        # RESULTADO_CONDICION_VERDADERA if CONDICION else RESULTADO_CONDICION_FALSA
        return {'message': 'Categoria no existe'} if categoria_encontrada is None else categoria_encontrada
    
    def get(self, id):
       
        categoria_encontrada = self.validarCategoria(id)

        # Si el tipo de dato que retorna el metodo validarCategoria, es un dict, entonces vamos a retornar 
        # ese contenido, caso contrario procedemos
        # type > podemos validar el tipo de dato de la variable y usarlo para condicionales
        if type(categoria_encontrada) == dict:
            return categoria_encontrada

        serializador = CategoriaSerializer()
        resultado = serializador.dump(categoria_encontrada)
        return {
            'content': resultado
        }
    def put(self, id):
         categoria_encontrada = self.validarCategoria(id)
        # Si el tipo de dato que retorna el metodo validarCategoria, es un dict, entonces vamos a retornar 
        # ese contenido, caso contrario procedemos
        # type > podemos validar el tipo de dato de la variable y usarlo para condicionales
         if type(categoria_encontrada) == dict:
            return categoria_encontrada
         data = request.get_json()
         serializador = CategoriaSerializer()
         try:
             data_validada = serializador.load(data)
             # hacemos las modificaciones de los valores de registro
             categoria_encontrada.nombre = data_validada.get('nombre')
             # Si me esta enviando la disponibilidad, la cambiaré, caso contrario, usaré la q tengo actualmente en la BD

             # Con el is not none, indicamos que la condicion será verdadera, si el contenido de la variable no es none, o sea puede ser falso, 0
             # u otro valor
             categoria_encontrada.disponibilidad = data_validada.get('disponibilidad') if data_validada.get(
                 'disponibilidad') is not None else categoria_encontrada.disponibilidad

             # procedemos con las actualizaciones
             conexion.session.commit()

             # transformamos la informacion para ser retornada
             resultado = serializador.dump(categoria_encontrada)

             return {
                'message': 'categoria actualizada correctamente',
                'content': resultado
                }
         except ValidationError as error:
             return {
                'message': 'Error al actualizar la categoria',
                'content': error.args
             }
    def delete(self, id):
         categoria_encontrada = self.validarCategoria(id)
        # Si el tipo de dato que retorna el metodo validarCategoria, es un dict, entonces vamos a retornar 
        # ese contenido, caso contrario procedemos
        # type > podemos validar el tipo de dato de la variable y usarlo para condicionales
         if type(categoria_encontrada) == dict:
            return categoria_encontrada
         
         # Eliminamos el registro de la BD
         conexion.session.delete(categoria_encontrada)

         # Para que sea de manera permanente
         conexion.session.commit()

         return {
             'message': 'Categoria eliminada exitosamente'
         }