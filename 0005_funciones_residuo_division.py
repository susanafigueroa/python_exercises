#Crea una función 'calculaResidu' a la que pasamos por parámetro el dividendo y el divisor, y devuelve
#como resultado el residuo de la división

def calculaResidu(a ,b):
    result = a % b
    return result

dividendo = int(input('Introduce el dividendo '))

divisor = int(input('Introduce el divisor '))

op = calculaResidu(dividendo , divisor)

print(op)
