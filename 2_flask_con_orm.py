from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy # para obtener la conexion
# https://docs.sqlalchemy.org/en/20/core/type_basics.html#generic-camelcase-types
from sqlalchemy import Column, types # importamos la libreria Column para la tabla y types para los tipos de datos CamelCase
from flask_migrate import Migrate
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow.exceptions  import ValidationError
from sqlalchemy.exc import IntegrityError

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
    precio = Column(type_=types.Float(precision=2), nullable=False)
    # serie ... not null unique > SQL
    serie = Column(type_=types.Text, nullable=False, unique=True)
    disponible=Column(type_=types.Boolean, nullable=True)
        # Si queremos manejar un nombre en el backend, y otro nombre en la bd, con la propiedad 'name' 
        # indicamos como se llamara en la bd
    fechaVencimiento = Column(type_=types.Date, nullable=True, name='fecha_vencimiento')

    # para indicar como queremos que se llame la tabla sin modificar el nombre de la clase
    __tablename__ = 'productos'

class ProductoSchema(SQLAlchemyAutoSchema):
    class Meta:
        # Sirve para pasarle informacion a la clase de la cual estamos heredando pero sin la necesidad de modificar
        # como tal la instancia de la clase
        model = ProductoModel
        # Al indicar el modelo que se tiene que basar, podra ubicar todos los atributos y ver sus restricciones ( not null,
        # unico, tipo de datos, etc)

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
        serializador = ProductoSchema()
       # Primero leeremos la informacion proveniente del cliente
        # Convierte el JSON entrante a un diccionario para q pueda ser leido en python
        data=request.get_json()

        # Validara la informacion proveniente del frontend y nos dara un error si no cumple los requisitos
        try:
            serializador.load(data)

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
        except ValidationError as error:
            return {
            'message': 'Error al crear el producto',
            'content': error.args
        }
        except IntegrityError as error:
            # Si falla al momento de guardar a la bd y el producto ya existe, (porq el nombre es unico)
            return {
                'message': 'Error al crear producto',
                'content': 'El producto ya existe!'
            }
    elif metodo == 'GET':
    #     # establecemos una consulta de obtencion de datos
    #     # Select * from productos;
    #     productos=conexion.session.query(ProductoModel).all()
        productos = conexion.session.query(ProductoModel).all()

        serializador = ProductoSchema()
        # Cuando convertimos la informacion desde la bd a un dict utilizaremos el metodo dump
        # Cuando pasamos un arreglo de instancias tenemos que agregar el parametro many=true
        # ese parametro ayuda a que itere la lista y convierta cada unoa de las instancias
        resultado = serializador.dump(productos, many=True)

    #     print(productos[0].id)
    #     resultado=[]
    #     for producto in productos:
    #         informacion_producto={
    #             'id': producto.id,
    #             'nombre': producto.nombre,
    #             'precio': producto.precio,
    #             'serie': producto.serie,
    #             'disponible': producto.disponible,
    #             'fechaVencimiento': producto.fechaVencimiento
    #         }
    #         resultado.append(informacion_producto)
    #     print(informacion_producto)
        return {
            'message': 'Los productos son',
            'content': resultado
            }

if __name__ == "__main__":
    app.run(debug=True)