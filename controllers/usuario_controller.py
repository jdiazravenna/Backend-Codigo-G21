from flask_restful import Resource, request
from models import Usuario
from instancias import conexion
from .serializers import RegistroSerializer, LoginSerializer, ActualizarUsuarioSerializer
from marshmallow.exceptions import ValidationError
from bcrypt import gensalt, hashpw, checkpw
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity


class RegistroController(Resource):
    def post(self):
        data = request.get_json()
        serializador = RegistroSerializer()
        try:
            data_serializada = serializador.load(data)
            # Generar el hash de la password para guardarla en la BD
            salt = gensalt() # convertimos nuestro password en seguro hasheado
            password_hashed = hashpw(bytes(data_serializada.get('password'), 'utf-8'), salt).decode('utf-8')

            # Ahora reemplazamos el valor del password, con el hasheo de la password
            data_serializada['password'] = password_hashed

            nuevo_usuario = Usuario(**data_serializada)
            conexion.session.add(nuevo_usuario)
            conexion.session.commit()
            return {
                'message': 'Usuario registrado correctamente',
                'content': serializador.dump(nuevo_usuario)
            }
        
        except ValidationError as error:
            return{
                'message': 'Error al registrar el usuario',
                'content': error.args
            }
        
class LoginController(Resource):
     def post(self):
        data = request.get_json()
        serializador = LoginSerializer()
        try:
            data_serializada = serializador.load(data)
            # Buscamos si el usuario existe en la BD
            usuario_encontrado = conexion.session.query(Usuario).filter(
            Usuario.correo == data_serializada.get('correo')).first()
            if usuario_encontrado is None:
                return{
                    'message': 'Usuario no existe'
                }
            password_en_bytes = bytes(data_serializada.get('password'), 'utf-8')
            password_bd_en_bytes = bytes(usuario_encontrado.password, 'utf-8')

            # El checkpw contrastara la password guardada en la BD, con la password enviada en el login,
            # y si es, retornara True, caso contrario, sera False
            resultado = checkpw(password_en_bytes, password_bd_en_bytes)
            if resultado == True:
                # indentity > es el identificador para reonocer a que usuario le pertenece ese token
                # El identificador de la Token, siempre debe ser un String
                token = create_access_token(
                    identity=str(usuario_encontrado.id))
                return {
                    'message': 'Bienvenido',
                    'token': token
                }
            else:
                return{
                    'message': 'Credenciales incorrectas'
                }
        except ValidationError as error:
            return {
                'message': 'Error al hacer login',
                'content': error.args
            }
        
class UsuarioController(Resource):
    @jwt_required()
        # Este metodo get sera una ruta PROTEGIDA, ed decirm se necesitara una token de acceso para poder
        # ingresar al controlador, caso contrario, sera rechazada la peticion
    def get(self):
         identificador = get_jwt_identity()
         
         print(identificador)
         # comparamos el usuario de la BD con el ID obtenido en el identificador
         usuario_encontrado = conexion.session.query(Usuario).filter(Usuario.id == identificador).first()

         if usuario_encontrado is None:
             return {
                 'message': 'El usuario no existe'
             }
         serializador = RegistroSerializer() # Reutilizamos el RegistroSerializer()
         resultado = serializador.dump(usuario_encontrado)

         return {
            'content': resultado # Retornar el usuario
        }

    @jwt_required()
    def put(self):
        identificador = get_jwt_identity()
         
        print(identificador)
        # comparamos el usuario de la BD con el ID obtenido en el identificador
        usuario_encontrado = conexion.session.query(Usuario).filter(Usuario.id == identificador).first()

        if usuario_encontrado is None:
             return {
                 'message': 'El usuario no existe'
             }
        serializador = ActualizarUsuarioSerializer()
        try:
            data_serializada = serializador.load(request.get_json())
            # Si el valor es un String vacio, no modificara la informacion,
            # asi lo maneja pyhton e ingresaremos al Else
            usuario_encontrado.nombre = data_serializada.get('nombre') if data_serializada.get('nombre') else usuario_encontrado.nombre

            usuario_encontrado.apellido = data_serializada.get('apellido') if data_serializada.get('apellido') else usuario_encontrado.apellido

            if data_serializada.get('password'):
                salt=gensalt()
                password_en_bytes = bytes(data_serializada.get('password'), 'utf-8')

                password_hasheada = hashpw(password_en_bytes, salt).decode('utf-8')

                usuario_encontrado.password = password_hasheada
            conexion.session.commit()

            return {
                'message': 'Usuario Actualizado Exitosamente'
            }
        except ValidationError as error:
            return {
                'message': 'Error al actualizar el usuario',
                'content': error.args
            }
