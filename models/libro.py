from instancias import conexion
from sqlalchemy import Column, types, ForeignKey
from datetime import datetime

class Libro(conexion.Model):
    id = Column(type_=types.Integer, autoincrement=True, primary_key=True)
    titulo = Column(type_=types.Text, nullable=False)
    descripcion = Column(type_=types.Text)
    cantidad = Column(type_=types.Integer)
    disponible = Column(type_=types.Boolean)
    # Si en el valor por default, ejecutamos la funcion, su valor sera el resultado de la funcion al momento
    # de crear la columna.
    # Sin embargo si solo declaramos la funcion, su valor por defecto sera la ejecucion de la funcion cada cez q se 
    # quiera ingresar un nuevo registro
    fecha_creacion = Column(type_=types.TIMESTAMP, default=datetime.now)
    categoriaId = Column(ForeignKey(column='categorias.id'),
                         type_=types.Integer, nullable=False, name='categoria_id')

    __tablename__ = 'libros'