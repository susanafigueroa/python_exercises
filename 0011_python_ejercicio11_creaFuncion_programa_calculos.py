#Queremos hacer un programa para hacer cálculos.
#El programa muestra un pequeño menú y cada opción nos pedirá uno o dos números
#para hacer un cálculo determinado.

def suma(a, b):
    return a+b

def resta(a, b):
    return a-b

def multi(a, b):
    return a*b

def div(a, b):
    return a/b

def residuo(a, b):
    return a%b

def cociente(a, b):
    return a//b

#creación del programa

programa = True

while( programa==True ):
    print('Escribe S si quieres sumar dos numeros')
    print('Escribe R si quieres restar dos numeros')
    print('Escribe M si quieres multiplicar dos numeros')
    print('Escribe D si quieres dividir dos numeros')
    print('Escribe O si quieres el residuo de la division de dos numeros')
    print('Escribe C si quieres el cociente de la division de dos numeros')
    a = int(input('Introduce el valor a'))
    b = int(input('Introduce el valor b'))
    x = str(input('¿Que quieres hacer?'))
    if x == 'S':
        print('La suma de ' ,a, ' y ' ,b, ' es ' ,suma(a, b))
    elif x == 'R':
        print('La resta de ' ,a, ' y ' ,b, ' es ' ,resta(a, b))
    elif x == 'M':
        print('La multi de ' ,a, ' y ' ,b, ' es ' ,multi(a, b))
    elif x == 'D':
        print('La div de ' ,a, ' y ' ,b, ' es ' ,div(a, b))
    elif x == 'O':
        print('La residuo de ' ,a, ' y ' ,b, ' es ' ,residuo(a, b))
    elif x == 'C':
        print('El cociente de ' ,a, ' y ' ,b, ' es ' ,cociente(a, b))
    if ((x == '0') or (a == 0) or (b == 0)):
        programa = False

