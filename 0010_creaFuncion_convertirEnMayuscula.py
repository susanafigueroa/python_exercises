#Crea una función 'aMayuscula' que dado un carácter cualquiera:
#a) devuelva el carácter convertido en mayúscula en caso de ser letra
#b) lo deje tal cual si no es letra
#rango ASCI para carácteres letra: del 97 al 122

def aMajuscula(x):
    if ( ord(x) <= 122 and ord(x) >= 97 ):
        return x.capitalize()
    else:
        return x

x = input('enter a character')

print(aMajuscula(x))
