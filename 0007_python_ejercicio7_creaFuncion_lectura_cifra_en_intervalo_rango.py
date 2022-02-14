#Crea función 'lecturaIntervalo' que haga una lectura de una cifra dentro de un intervalo. A la función le
#pasaremos el valor mínimo del rango, el valor máximo, y nos devolverá un valor leído del telado
#que esté dentro de este rango. Como en el ejercicio anterior, hasta que el número no esté dentro del intervalo,
#la función continuará pidiendo el número al usuario.

def lecturaIntervalo(min, max, number):
    min = int(input('enter the min value of the rang'))
    max = int(input('enter the max value of the rang'))
    number = int(input('enter the number'))
    while (not (number < max and number > min)):
        number = int(input('enter the number'))
    return number

min = 0
max = 0
number = -1

op = lecturaIntervalo(min, max, number)

print(op)


