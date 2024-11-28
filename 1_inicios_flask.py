from flask import Flask, request
from psycopg import connect

# __name__ > propia de python que sirve para indicar si el archivo en el cual nos encontramos
# es el archivo principal (el q se esta ejecutando por la terminal).
# si es el archivo principal, su valor será '__main__' caso contrario, tendrá otro valor variable

app = Flask(__name__)
# Flask solamente puede tener una instancia en todo el proyecto y esa instancia debe estar en el archivo principal
# si no no podra ejecutarse la instancia de la clase

# Para conectarse a la bd:
# Formato standar para las conexion a las bd
# DIALECTO://USUARIO:PASSWORD@HOST:PUERTO/DATABASE_NAME
# conexion = connect(dsn='postgresql://postgres:44787033@localhost:5432/finanzas')

# CONTRASEÑA POSTGRES 447870
conexion = connect(
    conninfo='postgresql://postgres:447870@localhost:5432/finanzas')

@app.route('/')
def incio():
    return 'Bienvenido a mi aplicacion de Flask!'
# Mediante el uso de decoradores, podemos indicar la ruta y cual sera su comportamiento
# Un decorador sirve para pdoer reusar un metodo de una clase, pero sin la necesidad de editarlo
# como tal, solamente se modificae l funcionamiento para, en este caso, la ruta configurada
# La funcionalidad de nuestro servidor, debe ir antes del metodo .run

@app.route('/inicio', methods=['POST'])
def inicio_aplicacion():
    return {
        'message': 'Bienvenido, acabas de ingresar a mi Endpoint @JTech!'
    }

# Si queremos recibir un parametro por la URL q sea dinamico, este parametro tiene q estar entre < >
# Adicional a ello, se puede indicar el tipo de dato (int, string)
@app.route('/usuarios/<int:id>', methods=['GET', 'POST'])
def mostrar_usuario(id):
    # Cuando pobnemos un parametro dinamico, entonces ese parametro tiene q ser registrado con el mismo nombre
    # como parametro de la funcion
    print(id)
    return {
        'message': f'El usuario es {id}'
    }

@app.route('/gestionar-usuario/<int:id>', methods = ['POST', 'PUT', 'DELETE'])
def gestionar_usuario(id):
    # Para poder manejar la informacion de la peticion se usa el metodo request de Flask
    if request.method == 'POST':
        return {
            'message': 'La creación del usuario, fué exitosa'
        }
    elif request.method == 'PUT':
        return {
            'message': 'Usuario actualizado correctamente'
        }
    elif request.method == 'DELETE':
        return {
            'message': 'El usuario fué eliminado correctamente'
        }

@app.route('/listar-clientes', methods=['GET'])
def listar_clientes():
    cursor = conexion.cursor()
    cursor.execute("select * from clientes")
    # para obtener la informacion proveniente del select
    # fetchall() > devuelve todos los registros del select
    # fetchmany(limite) > devuelve los registros hasta el limite
    # fetchone() > Devuelve el primer registro del select
    data=cursor.fetchall()
    print(data)
    return {
        'message': ' los clientes son'
    }

# levanta el servidor de flask con algunos parametros opcionales.
# debug > si su valor es true, entonces cada vez q modifiquemos el servidor y guardamos
# este se reiniciará automaticamente
app.run(debug=True)