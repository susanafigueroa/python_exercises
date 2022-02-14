#Crea una función 'esDigit' que dado un carácter cualquiera nos diga si es numérico o no.
#La función recibe un parámetro que representará un único carácter, y devolverá un valor entero.
# I si el carácter es un número
# 0 si el carácter NO es un número
# en código asci el carácter '0' equivale al 48
# en código asci el carácter '9' equivale al 57

def esDigit(x):
    if (ord(x) >= 48 and ord(x) <= 57):
        return 1
    else:
        return 0

a = True

while (a == True):
    x = input('enter a character')
    if (esDigit(x) == 1):
        a = False
        print('the character is a number')
    else:
        print('the character is not a number')