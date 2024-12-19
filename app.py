from flask import Flask
from instancias import conexion
from os import environ
from dotenv import load_dotenv
from flask_migrate import Migrate
from models import *
from controllers import *
from flask_restful import Api
from flask_jwt_extended import JWTManager
from datetime import timedelta

load_dotenv() # carga las variables de entorno .env

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL_PRINCIPAL')

# Aca agregamos las otras conexiones a otras bases de datos secundarias
app.config['SQLALCHEMY_BINDS'] = {
    'mysql': environ.get('DATABASE_URL_MYSQL')
}
# Cuando utilizamos la libreria JWT, tenemos q definir las configuraciones en nuestra variable
app.config['JWT_SECRET_KEY'] = environ.get('JWT_SECRET')
# le aumentamos el tiempo de duracion al token
app.config['JWT_ACCESS_TOKEN_EXPIRES']=timedelta(hours=3, minutes=5, seconds=10)
JWTManager(app)

conexion.init_app(app)

Migrate(app, conexion) # llamamos con la libreria migrate

api = Api(app)
# agregamos los recursos
api.add_resource(CategoriaController, '/categorias')
api.add_resource(RegistroController, '/registro')
api.add_resource(LoginController, '/login')
api.add_resource(UsuarioController, '/usuario')

if __name__ == '__main__':
    app.run(debug=True)