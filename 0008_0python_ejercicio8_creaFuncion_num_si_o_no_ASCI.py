#Crea una función 'esDigit' que dado un carácter cualquiera nos diga si es numérico o no.
#La función recibe un parámetro que representará un único carácter, y devolverá un valor entero.
# I si el carácter es un número
# 0 si el carácter NO es un número
# en código asci el carácter '0' equivale al 48
# en código asci el carácter '9' equivale al 57

def esDigit(x):
    while (not(ord(x) >= 48 and ord(x) <=57)):
        answ = print(0)
        x = input('enter a number')
    answ = 1
    return answ

x = input('enter a number')

op = esDigit(x)

result = print(op)
