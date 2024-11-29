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
# como tal, solamente se modificar el funcionamiento para, en este caso, la ruta configurada
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
            'message': f'La creación del usuario {id}, fué exitosa'
        }
    elif request.method == 'PUT':
        return {
            'message': f'Usuario {id} actualizado correctamente'
        }
    elif request.method == 'DELETE':
        return {
            'message': f'El usuario {id} fué eliminado correctamente'
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
    resultado=[] #creamos variable
    for registro in data:
        informacion_cliente={
            'id': registro[0],
            'nombre': registro[1],
            'correo': registro[2],
            'status': registro[3],
            'activo': registro[4],
            'fechaCreacion': registro[5]
        }
        print(informacion_cliente)
        resultado.append(informacion_cliente)

    return {  
        'message': 'Los clientes son',
        'content': resultado
     }      
       
# Crear un endpoint en el cual sirva para devolver un cliente por su ID
# /cliente/1 > Rodrigo
@app.route('/cliente/<int:id>')
def devolver_cliente(id):
    # primero me conecto a la BD
    cursor=conexion.cursor()
    #ejecuto la consulta para obtener el cliente
    cursor.execute(f'Select * from clientes where id = {id}')
    cliente_encontrado=cursor.fetchone()
    # print(cliente_encontrado)
    if cliente_encontrado is None:
        return {
            'message': 'El cliente no existe'
        }
    resultado = {
        'id': cliente_encontrado[0],
        'nombre': cliente_encontrado[1],
        'correo': cliente_encontrado[2],
        'status': cliente_encontrado[3],
        'activo': cliente_encontrado[4],
        'fechaCreacion': cliente_encontrado[5]
        
    }
    return {
        'message': 'Cliente encontrado',
        'content': resultado
    }
  
    
# levanta el servidor de flask con algunos parametros opcionales.
# debug > si su valor es true, entonces cada vez q modifiquemos el servidor y guardamos
# este se reiniciará automaticamente
app.run(debug=True)