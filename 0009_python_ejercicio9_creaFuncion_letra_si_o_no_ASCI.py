#Crea una función 'esLetra' que, dado un carácter cualquiera, nos diga si es una letra o no.
#La función recibe un parámetro, y devuelve un valor entero (1 si es una letra, 0 si no lo es).
#Lo primero que busco es el rango de los carácteres letras en asci:
#del 97 al 122

def esLetra(x):
    if ( ord(x) <= 122 and ord(x) >= 97 ):
        return 1
    else:
        return 0

x = input('enter a character')

if (esLetra(x) == 1):
    print('the character is a letter')
else:
    print('the character is not a letter')
