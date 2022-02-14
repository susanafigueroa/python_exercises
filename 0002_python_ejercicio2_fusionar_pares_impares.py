#Haz un programa que fusione los archivos pares e impares en un archivo llamado: '1a100.txt'

pares = open('pares.txt', 'r+')
impares = open('impares.txt', 'r+')

#fusiono ambos archivos: 'pares.txt' con 'impares.txt' usando el método

#fusion = open('1a100.txt', 'w+')

fusion = open('1a100.txt', 'r+')

#for i in pares:
#    fusion.write(str(i))

#for i in impares:
#    fusion.write(str(i))

fusion.seek(0)
print(fusion.read())