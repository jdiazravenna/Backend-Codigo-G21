from sqlalchemy import Column, types
from instancias import conexion
from enum import Enum

class TipoUsuario(Enum):
    # Creamos el enumerable, sobre los posibles valores que puede aceptar la columna
    ADMIN = 'ADMIN'
    CLIENTE = 'CLIENTE'
    EMPLEADO = 'EMPLEADO'

class Usuario(conexion.Model):
    id = Column(type_=types.Integer, autoincrement=True, primary_key=True)
    nombre = Column(type_=types.Text)
    apellido = Column(type_=types.Text)
    # En mysql, no puede haber una columna q sea texto y q sea unica
    # Ahora usaremos una columna VARCHAR como limite definido de 100
    # caracteres
    correo = Column(type_=types.String(100), unique=True, nullable=False)
    password = Column(type_=types.Text, nullable=False)
    tipo_usuario = Column(type_=types.Enum(TipoUsuario),
                          default=TipoUsuario.CLIENTE)
    
    __tablename__ = 'usuarios'

    # Si esta tabla sera creada y manejada en otra conexion que no es la predeterminada
    # entonces, usaremos la variable __bind_key__ para indicar que conexion debe usar
    __bind_key__ = 'mysql'