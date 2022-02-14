#Crea una función 'llegeix1a10' que se encargue de pedir al usuario que introduzca
#por teclado un número entre 0 y 10. Hasta que el número no esté entre 0 y 10, sigue pidiendo
#al usuario el número.
#La función no tiene parámetros y devuelve un número entero, que es el que ha leído la función.

def llegeix1a10(a):
    while (not (a < 10 and a > 0)):
        a = int(input('Introduce un numero que este entre el 0 y el 10'))
    return a

b = int(input('Introduce un numero que este entre el 0 y el 10'))

op = llegeix1a10(b)

print(op)

