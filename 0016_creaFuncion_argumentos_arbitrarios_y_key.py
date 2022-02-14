#Crea una función que tenga argumento, argumento arbitrario y argumento key.

def tiposArgumentos(argumento1 = '', *argumento2, **argumento3):
    print(argumento1)

    for i in argumento2:#se recorre como una teula
        print(i)

    for key in argumento3:#se recorre como un diccionario
        print('en la key',key,'se encuentra',argumento3)

tiposArgumentos('manzana', 'pera', 'platano', key1='carne', key2='pescado')
