# numero1 = 60
# numero2 = 60

# #     40   >    60   -> F
# if numero1 > numero2:
#     # si la condicion se cumple
#     print('en efecto se debe agregar a la bd')
# elif numero1 == numero2:
#     # si la primera condicion no se cumple podemos hacer una segunda validacion
#     print('no debemos hacer nada')
# # elif ...
# else:
#     # si la condicion no se cumplio
#     print('debemos solicitar los registros')


# num_ventas = 30

# if num_ventas >= 50:
#     print('dscto del 20%')
# elif num_ventas >= 30:
#     print('dscto del 10%')
# elif num_ventas >= 20:
#     print('dscto del 5%')
# else:
#     print('dscto del 2%')


# crear una funcion llamada resultado_final en la cual se reciba el nombre del alumno y su nota
# si la nota es entre 20 y 18 entonces el alumno tiene felicitacion publica
# si la nota es entre 15 y 17 el alumno esta aprobado y exonerado de la exposicion final
# si la nota es entre 11 y 14 el alumno esta aprobado
# si la nota es menor o igual que 10 entonces el alumno esta jalado

def resultado_final(alumno, nota):
    mensaje = ''
    if nota <= 20 and nota > 17:
        mensaje = f'El Alumno  {alumno}  Está aprobado y tiene felicitaciones publicas'
    elif nota > 14 and nota <= 17:
        mensaje = f'El alumno  {alumno} esta aprobado y exonerado de la exposicion final'
    elif nota > 10 and nota < 15:
        mensaje = f'El alumno {alumno} Esta Aprobado'  
    else:
        mensaje = f'El alumno {alumno}  Esta Desaprobado'
    return mensaje
    
resultado = resultado_final('juan', 18)
print(resultado)
resultado = resultado_final('juan', 15)
print(resultado)
resultado = resultado_final('juan', 14)
print(resultado)
resultado = resultado_final('juan', 10)
print(resultado)
    
        
# al final retornar un mensaje diciendo 'El alumno EDUARDO esta 'aprobado y exonerado de la exposicion final' > 15 y 17
    
# deadline Miercoles 20/11 18:59:59:59