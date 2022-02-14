#Amplia un programa existente que gestiona ficheros, de manera que se integren
#nuevas funcionalidades. Crea un programa que incorpore las funciones:
#delNomFitxer -> que borra el fichero de la carpeta actual llamado 'nomFitxer'
#propNomFitxer -> muestra las propiedades de un fichero -> su medida

import os

#creo la función que encontrará el archivo y lo eliminará
def delNomFitxer(a):
    for ruta, directori, arxius in os.walk('.'):
        if a in arxius:
            rutaAbs = os.path.join('.', ruta, a)
            return os.remove(rutaAbs)

#creo la función que encontrará el archivo y dirá sus propiedades
def propNomFitxer(a):
    for ruta, directori, arxius in os.walk('.'):
        if a in arxius:
            rutaAbs = str(os.path.join('.', ruta, a))
            size = print(os.path.getsize(rutaAbs))
            return size

#creación del programa
programa = True #creo un boolean para salir del programa cuando sea falso

while( programa==True ):
    a = str(input('Introduce el nombre del fichero al que le quieres hacer modificaciones'))
    print('Escribe D si quieres borrar el fichero de la carpeta donde se encuentra actualmente')
    print('Escribe P si quieres mostrar las propiedades del fichero')
    x = str(input('¿Que quieres hacer?'))
    if x == 'D':
        delNomFitxer(a)
        print('El fichero', a, 'ha sido eliminado.')
        programa = False
    elif x == 'P':
        propNomFitxer(a)
        print('Las propiedades del fichero', a, 'han sido mostradas.')
        programa = False