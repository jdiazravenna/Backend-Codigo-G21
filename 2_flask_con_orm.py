from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy # para obtener la conexion
# https://docs.sqlalchemy.org/en/20/core/type_basics.html#generic-camelcase-types
from sqlalchemy import Column, types # importamos la libreria Column para la tabla y types para los tipos de datos CamelCase

app=Flask(__name__)
# configuramos la cadena de conexion, agregamos la variable de conexion a nuestra BD
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg://postgres:447870@localhost:5432/bd_flask'
conexion = SQLAlchemy(app=app)

# Cada tabla que vayamos a crear, será como una clase
class ProductoModel(conexion.Model):
    # Herencia: semana 1 Programacion Orienada a Objetos
    # Ahora declaramos las columnas de la tabla, como si fueran atributos de la clase
    id = Column(type_=types.Integer, primary_key=True, autoincrement=True)
    # nombre ... not null, > SQL
    nombre = Column(type_=types.Text, nullable=False)
    # precio ... not null > SQL
    precio = Column(type_=types.Float, nullable=False)
    # serie ... not null unique > SQL
    serie = Column(type_=types.Text, nullable=False, unique=True)
    disponible=Column(type_=types.Boolean, nullable=True)

# creamos el decorador/endpoint para la ejecucion de la creacion de tablas en la BD
@app.route('/crear-tablas')
def crear_tablas():
    # Crea todas las tablas de la BD
    conexion.create_all() # siempre debe estar dentro de un decorador
    return {
        'message': 'Las tablas fueron creadas satisfactoriamente'
    }


app.run(debug=True)