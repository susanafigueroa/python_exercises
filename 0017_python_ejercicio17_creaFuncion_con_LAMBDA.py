#Crea 3 funciones distintas usando lambda:
#ejemplo:
#formaLambda2 = (Lambda x, n: x+n, Lambda x, n: x + n)

#función que sume 3 números

a = 10
n = 2

print('primer ejemplo:')

sumaLambda = lambda a, n: a + n

print('crida 1:',sumaLambda(a,a)) # 10 + 10 = 20
print('crida 1.2:',sumaLambda(a,n)) # 10 + 2 = 12

#otro ejemplo de función lambda

print('segundo ejemplo:')

sumaLambda = (lambda a, n: a + n, lambda a, n: a - n)

print('crida 1:',sumaLambda[0](a,a)) # 10 + 10 = 20
print('crida 1.2:',sumaLambda[0](a,n)) # 10 + 2 = 12
print('crida 2:',sumaLambda[1](a,a)) # 10 - 10 = 0
print('crida 2.1:',sumaLambda[1](a,n)) # 10 - 2 = 8


