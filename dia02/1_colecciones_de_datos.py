# Listas o arregles (arrays) []
#Ordenada y editable
frutas = ['manzana','platano','papaya','pitahaya']

#Ordenado > cada elemento de la lista esta en uns posicion determinada
print(frutas[2]) # papaya

#Editable > agregar y eliminar elementos de la lista
#El metodo remove solamente si existe ese elemento lo eliminara, si no, lanzara un error
frutas.append('mandarina')
frutas.append('piña')

print(len(frutas))

frutas.remove('papaya')

#El metodo pop funciona con la posicion de la fruta o palabra

frutas.pop(0)
print(frutas)

#Colocado como primer parametro el indice donde se agregara el nuevo conenido y segundo parametro el contenido a agregar
frutas.insert(2, 'sandia')
print(frutas)

# tupla ()
#No son editables, una vez creada, ya no se pueden editar
#Son ordenadas
alumnos = ('Farit', 'Francesca', 'Cesar', 'Christian', 'Eddy')
print(alumnos[0])
#alumnos[0] = 'Vanessa' #no se puede hacer

#Otra forma de crear una lista en base a una tupla, pero la tupla original sigue siendo tupla q no se puede editar

copia_alumnos = list(alumnos)
print(id(alumnos))
print(id(copia_alumnos))

copia_alumnos[0] = 'Gerson'
print(copia_alumnos)
segunda_copia=tuple(copia_alumnos)
print(id(segunda_copia))

#cuando copiamos una lista a otra variable, lo que estamos haciendo en realidad es utilizar la misma posicion de memoria
otras_frutas = frutas

#ahora hago unha copia del contenido y esto indica que se guarde en otra posicion de memoria
otras_frutas=frutas[:]


print(id(otras_frutas))
print(id(frutas))

print(otras_frutas)

frutas[1] = 'Fruta del dragon'
print(otras_frutas)

#Set {}
#es desordenada, es editable

inventario = {
    'monitores',
    'mouse',
    'proyectores',
    'cooler',
    'teclados'
}
print(inventario)
#No se puede realizar porque no es una coleccion de datos ordenada
#print(inventario[2])
#se puede usar para guardar configuraciones de una aplicación
print('monitores' in inventario)
print('Chicle' in inventario)

inventario.add('memoria ram')
inventario.remove('mouse')
print(inventario)

#Diccionary - Diccionarios
#Ordenado, pero por llaves, no por posicion ni indices
#Editable

persona = {
    'nombre' : 'Juan',
    'apellido' : 'Díaz',
    'email' : 'jjdiazsoluciones@gmail.com',
    'hobbies' : ['comer', 'programar', 'futbol'],
    'dirección' : {
        'calle' : 'jose Santos atahualpa',
        'numero' : 862,
        'postal' : '15302'
    },
    'viudo' : False,
    'familiares' : ('joao diaz', 'carlos diaz', 'william diaz')
}
print(persona['nombre'])

# Quiero ver los hobbies de la persona
print(persona['hobbies'])
# quiero ver cuandos hobbies tiene la persona (numeros)
print(len(persona['hobbies']))
# quiero ver en que calle vive la persona
print(persona['dirección'])
# quiero saber si es viudo o no
print(persona.get('viudo'))
# quiero saaber si maria washington es familiar o no
print('Washington' in persona['familiares'])

curso = {
    'nombre': 'Backend',
    'duracion': '10 semanas',
    'fecha_inicio': '2024-11-11',
    'fecha_fin': '2025-01-30',
    'topics': ['Python', 'Express', 'Django', 'Flask'],
    'semanas': [
        {
            'nombre': 'semana 01',
            'descripcion': 'intro a python'
        },
        {
            'nombre': 'semana 02',
            'descripcion': 'base de datos'
        }
    ],
    'habilidades': ('logica de programacion', 'manejo de eventos', 'despliegue en servidores'),
    'finalizado': False,
    'profesores': {
        'Arnold Gallegos', 'Eduardo de Rivero'
    },
    'costo': 550.76,
    'descanso': 'a veces'
}

# nombre del curso y su duracion
print(curso['nombre'], curso['duracion'])
# cuantos topics tiene el curso
print(len(curso['topics']))
# muestrame los 2 primeros topics
print(curso['topics'][0:2])
# cuantas semanas tiene en el
print(len(curso['semanas']))
# descripcion de la semana 01
print(curso['semanas'][0]['descripcion'])
# 'manejo de eventos' es parde de las habilidades?
print('Manejo de habilidades' in curso['habilidades'])
# enseñara el profesor "Juan martinez"?
print('Juan Martinez' in curso['profesores'])