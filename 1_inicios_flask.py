from flask import Flask

# __name__ > propia de python que sirve para indicar si el archivo en el cual nos encontramos
# es el archivo principal (el q se esta ejecutando por la terminal).
# si es el archivo principal, su valor será '__main__' caso contrario, tendrá otro valor variable

app = Flask(__name__)
# Flask solamente puede tener una instancia en todo el proyecto y esa instancia debe estar en el archivo principal
# si no no podra ejecutarse la instancia de la clase

# levanta el servidor de flask con algunos parametros opcionales.
# debug > si su valor es true, entonces cada vez q modifiquemos el servidor y guardamos
# este se reiniciará automaticamente
app.run(debug=True)