from flask import Flask
from instancias import conexion
from os import environ
from dotenv import load_dotenv
from flask_migrate import Migrate
from models import *
from controllers import *
from flask_restful import Api


load_dotenv() # carga las variables de entorno .env

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL_PRINCIPAL')

# Aca agregamos las otras conexiones a otras bases de datos secundarias
app.config['SQLALCHEMY_BINDS'] = {
    'mysql': environ.get('DATABASE_URL_MYSQL')
}
conexion.init_app(app)

Migrate(app, conexion) # llamamos con la libreria migrate

api = Api(app)
# agregamos los recursos
api.add_resource(CategoriaController, '/categorias')
api.add_resource(RegistroController, '/registro')
api.add_resource(LoginController, '/login')

if __name__ == '__main__':
    app.run(debug=True)