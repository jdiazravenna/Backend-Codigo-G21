#snake_case

nombre_completo = 'Juan Díaz Ravenna'

#camelCase
nombreCompleto='Juan Diaz Ravenna'

#PascalCase

NombreCompleto='Juan Diaz Ravenna'

#No se puede usar caracteres especiales - @ /

#nombre@completo = 'Juan Diaz'

#Los Strings se concatenan con +

nombre_completo = 'Juan' + 'Diaz'

#No se puede contatenar Strings con enteros o floats

#Accedemos a la posicion de los strings

nombhre = 'juan'
print(nombhre[2])

#Cantidad de caracteres

nombre_3 = 'Juan Jose'
longitud = len(nombre_3)
print(longitud)

#Se puede sacar un sub-String o una sub-cadena

texto='Hola esta es una prueba de texto para extraer'
# desde posicion 1 hasta posicion < 15
sub_texto = texto[1:15]
print(sub_texto)

# si colocamos [:] haremos una copia del contenido de la variable texto

sub_texto = texto[:]
sub_texto = texto
print(sub_texto)

#Numericos
resultado = 10 + 3.75
#forma para poder hacer mas legible un numero grande con la adherencia de '_'
#Solo sirve para lectura
#Esta ayuda esta disponible desde la version 3.6 en adelante
numerazo = 1_015_886_546_765_165
print(resultado)
print(numerazo)

numero100 = 3,75 #Se convierte en una Tupla

#otra forma de declarar variables
numero1, numero2 = 3, 75 #Se asigna un numero a cada variable
print(numero100)

#Boolean

libre = True
#En python para utilizar el operador '!', se debe usar el NOT
print(not libre)