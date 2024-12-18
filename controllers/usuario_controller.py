from flask_restful import Resource, request
from models import Usuario
from instancias import conexion
from .serializers import RegistroSerializer, LoginSerializer
from marshmallow.exceptions import ValidationError
from bcrypt import gensalt, hashpw, checkpw


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
                return {
                    'message': 'Bienvenido'
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