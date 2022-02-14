#Crea función que escriba los meses del año según la llamada de la función, ejemplo:
#primera llamada de la función -> que escriba Enero
#segunda llamada de la función -> que escriba Febrero
#tercera llamada de la función -> que escriba Marzo
#etc

def meses(nombre='', numero=0, temperatura=''):
    print(nombre)
    print(numero)
    print(temperatura)

mesesArray=['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Setiembre', 'Octubre', 'Noviembre', 'Diciembre']

for i in range(1,13):
    if (i <=3 and i >= 1) or (i <= 12 and i >= 10):
        meses(mesesArray[i-1], i, 'frio')
    else:
        meses(mesesArray[i-1], i, 'calor')



#meses('Enero', 1, 'frio')
#meses('Febrero', 2, 'frio')
#meses('Marzo', 3, 'frio')
#meses('Abril', 4, 'calor')
#meses('Mayo', 5, 'calor')
#meses('Junio', 6, 'calor')
#meses('Julio', 7, 'calor')
#meses('Agosto', 8, 'calor')
#meses('Setiembre', 9, 'calor')
#meses('Octubre', 10, 'frio')
#meses('Noviembre', 11, 'frio')
#meses('Diciembre', 12, 'frio')
