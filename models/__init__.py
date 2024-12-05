# Si queremos utilizar una carpeta como un conjunto de archivos, que podremos 
# utilizar en nuestro proyecto, lo que podemos hacer es, crear el archivo __init__.py, 
# para q podamos exportar todas las funcionabilidades en este archivo, y se pueden importar
# de una manera mas facil en otras partes del proyecto

# Si en nuestra sub carpeta queremos utilizar alguno de los archivos de esta, entonces ingresaremos
# a colocando un punto que sirve para indicar que accedemos desde nivel
from .categoria import CategoriaModel
from .producto import ProductoModel
from .prueba import PruebaModel

