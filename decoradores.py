def decorador_sin_parametros(funcion):
    def wrapper(*args, **kwargs):
        print(args)
        print(kwargs)
        # agregar funcionabilidad adicional antes de mandar a llamar a la funcion
        resultado = funcion(*args, **kwargs)
        # siempre se necesita retornar el resultado de la funcion para que se ejecute con normalidad
        return resultado

    return wrapper


# agregando funcionabilidad a la funcion saludar implementando la funcionabilidad del decorador creado
@decorador_sin_parametros
def saludar(nombre, **kwargs):
    return f'Hola {nombre}'


print(saludar('Eduardo', edad=32))


def decorador_con_parametros(limite):
    def decorador(funcion):
        def wrapper(*args, **kwargs):
            print(limite)
            resultado_general = []
            for numero in range(0, limite):
                resultado = funcion(*args, **kwargs)
                resultado_general.append(resultado)
            return resultado_general
        return wrapper
    return decorador


@decorador_con_parametros(5)
def sumar(numero1, numero2):
    return numero1 + numero2


print(sumar(10, 20))


# simulacion de los usuarios en la bd
usuarios = [{'nombre': 'Farit', 'alDia': True},
            {'nombre': 'Juanito', 'alDia': False}]


def validar_pagos(funcion):
    def wrapper(*args, **kwargs):
        # Simulamos que vamos a la bd y vemos si el usuario esta la dia en sus pagos
        nombre = args[0]
        print(nombre)
        for usuario in usuarios:
            if usuario.get('nombre') == nombre:
                if usuario.get('alDia') == True:
                    resultado = funcion(*args, **kwargs)
                else:
                    resultado = f'{
                        nombre} Por favor ponte al dia en tus pagos lo mas pronto posible'
        return resultado
    return wrapper


# los kwargs no son obligatorios
@validar_pagos
def saludar(nombre, **kwargs):
    return f'Hola {nombre}'


print(saludar('Farit', departamento='Judicial'))
print(saludar('Juanito', estatua=2.10))