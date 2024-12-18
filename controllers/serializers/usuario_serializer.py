from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from models import Usuario, TipoUsuario
from marshmallow_enum import EnumField
from marshmallow import Schema, fields

class RegistroSerializer(SQLAlchemyAutoSchema):
    # Si quiero modificar alguna columna del modelo para cuestiones del serializador
    # Ahora modificamos la columna password y le indicamos que tiene q ser requerida a la hora
    # de serializar
    password = auto_field(required=True, load_only=True)
    # la propiedad load_only, oculta la contraseña al momento de crear el nuevo usuario

    # modificar el comportamiento de la columna q sea enum, en la cual se le coloca
    # que enum debe utilizar para hacer las validaciones
    tipo_usuario = EnumField(TipoUsuario)
    class Meta:
        model = Usuario

class LoginSerializer(Schema):
    correo = fields.Email(required=True)
    password = fields.String(required=True)
