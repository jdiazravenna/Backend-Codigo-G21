from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy # para obtener la conexion
# https://docs.sqlalchemy.org/en/20/core/type_basics.html#generic-camelcase-types
from sqlalchemy import Column, types # importamos la libreria Column para la tabla y types para los tipos de datos CamelCase
from flask_migrate import Migrate

app=Flask(__name__)
# configuramos la cadena de conexion, agregamos la variable de conexion a nuestra BD
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg://postgres:447870@localhost:5432/bd_flask'
conexion = SQLAlchemy(app=app)

# luego de establecer la conexion utilizando SQLAlchemy, ahora utilizamos la clase Migrate
Migrate(app=app, db=conexion)

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
        # Si queremos manejar un nombre en el backend, y otro nombre en la bd, con la propiedad 'name' 
        # indicamos como se llamara en la bd
    fechaVencimiento = Column(type_=types.Date, nullable=True, name='fecha_vencimiento')

    # para indicar como queremos que se llame la tabla sin modificar el nombre de la clase
    __tablename__ = 'productos'

# creamos el decorador/endpoint para la ejecucion de la creacion de tablas en la BD
# @app.route('/crear-tablas')
# def crear_tablas():
#     # Crea todas las tablas de la BD
#     conexion.create_all() # siempre debe estar dentro de un decorador
#     return {
#         'message': 'Las tablas fueron creadas satisfactoriamente'
#     }

@app.route('/productos', methods=['POST','GET'])
def gestion_productos():
    metodo=request.method
    if metodo=='POST':
       # Primero leeremos la informacion proveniente del cliente
        # Convierte el JSON entrante a un diccionario para q pueda ser leido en python
        data=request.get_json()
        nuevoProducto=ProductoModel(nombre=data.get('nombre'),
                  precio=data.get('precio'),
                  serie=data.get('serie'),
                  disponible=data.get('disponible'),
                  fechaVencimiento=data.get('fechaVencimiento')
                  )

        print('Producto antes de guardarse en la bd', nuevoProducto.id)
        # Utilizamos la conexion para conectarnos a la bd
        # empezamos una transaccion, en la cual estamos indicando que agregaremos este registro
        conexion.session.add(nuevoProducto)

        # indicamos que los cambios tiene q guardase de manera permanente
        conexion.session.commit()

        print('Producto despues de guardarse en la bd', nuevoProducto.id)
        return {
        'message': 'Producto creado exitosamente'
        }
    elif metodo == 'GET':
        # establecemos una consulta de obtencion de datos
        # Select * from productos;
        productos=conexion.session.query(ProductoModel).all()

        print(productos)
        return {
            'message': 'Los productos son'
        }

if __name__ == "__main__":
    app.run(debug=True)