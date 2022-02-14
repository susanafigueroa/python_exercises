#Define y programa una función que, dados un precio y un porcentaje de descuento, nos devuelva el
#precio con el descuento aplicado. La función tiene dos parámetros : precio y porcentaje.
#Devuelve el precio con el descuento aplicado.

price = int(input('Enter the price'))

percent = int(input('Enter the % discount'))

def desc(a, b):
    calculo = a - (a*b/100)
    return calculo

op = desc(price, percent)

print(op)


