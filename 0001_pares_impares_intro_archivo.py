#Haz un programa que escriba en el archivo 'pares.txt' los nombres pares del 1 al 100
#y en 'impares.txt' del 1 al 100

pares = open('pares.txt', 'w+')
impares = open('impares.txt', 'w+')

for i in range(0, 101):
    if i % 2 == 0:
        pares.write(str(i) + ' ')
    else:
        impares.write(str(i) + ' ')

pares.seek(0)
print(pares.read())
pares.close()

impares.seek(0)
print(impares.read())
impares.close()
