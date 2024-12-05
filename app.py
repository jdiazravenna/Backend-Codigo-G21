from flask import Flask
from instancias import conexion
from os import environ
from dotenv import load_dotenv

# Revisara si hay algun archivo llamado .env y leerá las variables definidas en él, 
# y los colocará como variables de entorno
load_dotenv()

# De esta manera creamos nuestra instancia de Flask
app = Flask(__name__)

# app.config('SQLALCHEMY_DATABASE_URI') = ''

# Si vamos a tener, mas de una conexion, a diferentes bases de datos, entonces
# debemos utilizar la variable SQLALCHEMY_BINDS

app.config['SQLALCHEMY_BINDS'] = {
    'postgres': environ.get('DATABASE_URL'),
    # 'mysql': ''
}

# Asi se puede inicializar la conexion a la BD, desde otro archivo
conexion.init_app(app)

# Al momento de crear nuestro modelo (tabla) usaremos la variable __bind_key__ para
# indicar a que BD queremos utilizar

# class UsuarioPostgresModel(conexion.Model):
#   __bind_key__ = 'postgres'
#   id = Column(type_=types.integer)

if __name__ == '__main__':
    app.run(debug=True)