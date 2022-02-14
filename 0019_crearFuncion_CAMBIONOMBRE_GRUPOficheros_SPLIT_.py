#Exercici2: L'objectiu d'aquesta activitat és veure com canviar el nom a un conjunt de fitxers. Genereu un
# programa que pregunti a l'usuari dues cadenes de text de tres lletres, de manera que les pugui escriure pel
# teclat en una mateixa línia. El programa ha de cercar tots els fitxers en el seu directori de treball que
# tinguin com extensió la primera cadena de text i canviar-la a la segona. Per exemple, si l'usuari escriu
# 'txt jpg' tots els fitxers amb extensió '.txt' han de passar a tenir l'extensió '.jpg'

import glob
import os

quest = True

while (quest == True):
    string7 = input('Introdueix el tipus darxiu que vols modificar (3 char), espai, el tipus darxiu final (3 char):')
    if (len(string7) != 7):
        print('Thas equivocat, tornaho a probar.')
    else:
        quest = False

#Ara amb l'split separo les dos cadenes de 3 caràcters:

arrayType = string7.split()

oldType = '*.'+ arrayType[0] #m'ha de buscar els arxius d'aquest tipus

newType = '*.'+ arrayType[1] #el nou tipus que adquiriran els arxiu seleccionats

#selecciono tots els arxius que són de tipus oldType:

grupArxiusOldType = glob.glob(os.getcwd() + os.sep + oldType)

#ara vull modificar el tipus d'arxiu dels arxius seleccionats:
#creo una funció que em modifiqui els tipus d'arxius per grups d'arxius:

def canviTipusArxiusPerGrups(grupArxiusOld):
    for indx, arxiu in enumerate(grupArxiusOld):
        os.rename(arxiu, arxiu.replace(arrayType[0], arrayType[1]))
        #print(arxiu)
        #print(indx)

canviTipusArxiusPerGrups(grupArxiusOldType)

print('old final', glob.glob(os.getcwd() + os.sep + oldType))
print('new final', glob.glob(os.getcwd() + os.sep + newType))
