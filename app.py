from flask import Flask
from instancias import conexion
from os import environ
from dotenv import load_dotenv
from flask_migrate import Migrate
from models import *
from flask_restful import Api # Sera la encargada de gestionar todas las rutas de mi app
from controllers import *

# Revisara si hay algun archivo llamado .env y leerá las variables definidas en él, 
# y los colocará como variables de entorno
load_dotenv()

# De esta manera creamos nuestra instancia de Flask
app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL')

# Si vamos a tener, mas de una conexion, a diferentes bases de datos, entonces
# debemos utilizar la variable SQLALCHEMY_BINDS


app.config['SQLALCHEMY_BINDS'] = {
    'postgres': environ.get('DATABASE_URL2')
    # 'mysql': ''
}

# Asi se puede inicializar la conexion a la BD, desde otro archivo
conexion.init_app(app)

# Al momento de crear nuestro modelo (tabla) usaremos la variable __bind_key__ para
# indicar a que BD queremos utilizar

# class UsuarioPostgresModel(conexion.Model):
#   __bind_key__ = 'postgres'
#   id = Column(type_=types.integer)

Migrate(app=app, db=conexion)

# Declaracion de rutas
api.add_resource(CategoriaController, '/categorias')

if __name__ == '__main__':
    app.run(debug=True)