# Crear la clase producto model
# Id integer, pk, autoincrementable
# nombre, texto y no puede ser null
# descripcion text y puede ser null
# precio float, y no puede ser null
# disponibilidad boolean y su valor por defecto sea True
# nombre de la tabla sea 'productos'
# ademas agregar el bind_key

from instancias import conexion
from sqlalchemy import Column, types, ForeignKey

class ProductoModel(conexion.Model):
    id = Column(type_=types.Integer, primary_key=True, autoincrement=True)
    nombre = Column(type_=types.Text, nullable=False)
    descripcion = Column(type_=types.Text, nullable=True)
    precio = Column(type_=types.Float, nullable=False)
    disponibilidad = Column(type_=types.Boolean, default=True)

    # RELACIONES
    # En este caso estariamos utilizando una relacion de 1 a n
    categoriaId = Column(ForeignKey(column='categorias.id'),
                         type_=types.Integer, nullable=False)

    __tablename__ = 'productos'
    __bind_key__ = 'postgres'