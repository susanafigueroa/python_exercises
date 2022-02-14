#Crea un bucle que escriba el abecedario. Luego una función que multiplique el código asci de una de las letras
#por n veces.

for i in range(97, 123):
    print(chr(i))

#ahora el código de la función:

c = input('¿de que letra quieres repetir el codigo asci?')
d = int(input('¿cuantas veces quieres repetir el codigo asci?'))

def multiLetra(letra='', n = 0):
    return (str(ord(letra)) + ' ') * n

print(multiLetra(c, d))

#ahora para que la función haga el return con salto de linea

m = input('¿de que letra quieres repetir el codigo asci?')
b = int(input('¿cuantas veces quieres repetir el codigo asci?'))

def multiLetra(m='', b = 0):
    return (str(ord(m)) + '\n') * b

print(multiLetra(m, b))