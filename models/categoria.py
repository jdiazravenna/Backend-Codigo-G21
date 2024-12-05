from instancias import conexion
from sqlalchemy import Column, types
from datetime import datetime

class CategoriaModel(conexion.Model):
    id = Column(type_=types.Integer, autoincrement=True,
                primary_key=True, nullable=False)
    nombre = Column(type_=types.Text, nullable=False)
    fechaCreacion = Column(name='fecha_creacion', type_=types.TIMESTAMP, default=datetime.now)
    disponibilidad = Column(type_=types.Boolean, default=True)

# Creamos el nombre de la tabla
    __tablename__ = 'categorias'
    # Si en nuestra instamcia de sqlalchemy, estamos usando mas de un conector, entonces
    # debemos en cada tabla que usemos, indicar a que conexion nos referiremos, esto servira
    # para cuestiones de creeacion de tabla y para la lectura y modificacion de datos
    __bind_key__ = 'postgres'