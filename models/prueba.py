from instancias import conexion
from sqlalchemy import Column, types

class PruebaModel(conexion.Model):
    id = Column(type_=types.Integer, autoincrement=True, primary_key=True)
    nombre = Column(type_=types.Text)

    __tablename__ = 'pruebas'
    # Al no definir el atributo bind_key__, esta se creara en la BD por defecto
    # (SQLALCHEMY_DATABASE_URI)
    # Solamente se debe definir el __nind_key__ en las tablas que queremos crear en las otras
    # conexiones
    # __bind_key__ = 'postgres2'