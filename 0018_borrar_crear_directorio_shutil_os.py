#Feu un programa que actuï de manera diferent segons si existeix o no una carpeta anomenada 'Temp' a la seva
# carpeta de treball. Si no existeix, l'ha d'intentar crear. Si existeix, l'ha d'esborrar. Cada cop que es
# realitza una acció, cal dir si s'ha pogut dur a terme i la ruta absoluta de la carpeta processada.

import os
import shutil

print(os.getcwd())

if os.path.exists(r"C:\Users\shiun\PycharmProjects\pythonProject1\Temp"):
    shutil.rmtree('Temp')
    print('Sha esborrat la carpeta Temp')
else:
    os.mkdir('Temp')
    print('Sha creat la carpeta Temp')
