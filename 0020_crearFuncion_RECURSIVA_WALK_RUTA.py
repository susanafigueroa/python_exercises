#Exercici3: L'objectiu d'aquesta activitat és saber recórrer una jerarquia de carpetes i fitxers per
# realitzar operacions sobre ella. Feu un programa que pregunti per pantalla el nom d'un fitxer i el text
# de la ruta a una carpeta. Aquestes dades les introduirà l'usuari pel teclat. Llavors el programa ha de cercar
# i mostrar per pantalla la ruta absoluta de tots els fitxers amb aquest nom a partir de la carpeta
# assenyalada (tant directament dintre seu com dins d'altres carpetes successives).

#creo un arxiu dins la carpeta 'C:\Users\shiun\PycharmProjects\pythonProject1\venv\Libros' anomenat exercici3.txt
#newFile = open(r'C:\Users\shiun\PycharmProjects\pythonProject1\venv\Libros\exercici3.txt', 'w+')
#newFile = open(r'C:\Users\shiun\PycharmProjects\pythonProject1\venv\Libros\exercici3.txt', 'r+')

#creo un altre arxiu dins la carpeta 'C:\Users\shiun\PycharmProjects\pythonProject1\venv' anomenat exercici3.txt
#newFile = open(r'C:\Users\shiun\PycharmProjects\pythonProject1\venv\exercici3.txt', 'w+')
#newFile = open(r'C:\Users\shiun\PycharmProjects\pythonProject1\venv\exercici3.txt', 'r+')

#creo un altre arxiu dins la carpeta 'C:\Users\shiun\PycharmProjects\pythonProject1' anomenat exercici3.txt
#newFile = open(r'C:\Users\shiun\PycharmProjects\pythonProject1\exercici3.txt', 'w+')
#newFile = open(r'C:\Users\shiun\PycharmProjects\pythonProject1\exercici3.txt', 'r+')

import os

#per probar l'exercici introduiré el fitxer 'exercici3.txt'
nameFile = str(input('introdueix el nom dun fitxer'))

#per probar l'exercici introduiré la ruta 'C:\\Users\\shiun\\PycharmProjects'
rutaInici = str(input('introdueix el nom de la ruta a una carpeta'))

#creo la funció que buscarà el fitxer
#la funció os.walk permet caminar per l'arbre de directoris
def buscarFitxer(rutaInici, nameFile):
    for ruta, directori, arxius in os.walk(rutaInici):#la funció os.walk ens torna ruta, directori, arxius
        if nameFile in arxius:
            rutaAbs = os.path.join(rutaInici, ruta, nameFile)#per unir les diferents seccions de la ruta absoluta
            print(rutaAbs)
            return rutaAbs

buscarFitxer(rutaInici, nameFile)
