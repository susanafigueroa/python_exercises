#Crea una función que recorra argumento arbitrario y que recorra argumento arbitrario key.

def recorrerArbitrarios(argumento, *argumentoArbitrario, **argumentoArbitrarioKey):
    print(argumento)

    for i in argumentoArbitrario: #se recorre como una tupla
        print(i)

    for key in argumentoArbitrarioKey: #se recorre como un diccionario
        print('El valor de ',key,' es ', argumentoArbitrarioKey[key])

recorrerArbitrarios('hola1','hola2','hola3','hola4', key1='holakey1', key2='holakey2')

