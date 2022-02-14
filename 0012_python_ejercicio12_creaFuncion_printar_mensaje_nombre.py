#Crea una función que devuelva un 'Hola' nombre.

print('primera manera: ')

def saludo(mensaje, nombre):
    a = print(mensaje, nombre)
    return a

mensaje = input('introduce el mensaje')
nombre = input('introduce tu nombre')
saludo(mensaje, nombre)

print('segunda manera: ')

def saludo2(mensaje, nombre):
    a = print(mensaje, nombre)
    return a

saludo2(mensaje='Hola', nombre='Susana')