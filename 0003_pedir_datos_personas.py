#Haz un programa que pida datos de las personas
#nombre, apellido, NIF, edad, altura
#el proceso termina cuando el usuario indica que no quiere introducir más personas
#el programa tiene como mínimo las funciones:
#leerPersona
#escribirPersonaAlDisco

datos = open('datos.txt', 'r+')

exit = 'y'

datosArray = ['','','','','']

count = 0

row = 0

def leerPersona():
    global name
    name = input('enter your name: ')
    datosArray[count] = name
    lastName = input('enter your lastname: ')
    datosArray[count+1] = lastName
    NIF = input('enter your NIF: ')
    datosArray[count+2] = NIF
    age = input('how old are you: ')
    datosArray[count+3] = age
    height = input('what is your height: ')
    datosArray[count+4] = height

while exit == 'y':
    leerPersona()
    row = row + 1
    exit = input(' do you want to add another person? y or n')


print(datosArray)
