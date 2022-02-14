#Printa el factorial de n.

def numFactorial(n):
    nu = 1
    for i in range(n, 1, -1):
        nu = nu * i
        print (i, '*')
        if ( i == 2 ):
            print('1 =')
    return nu

num = int(input('enter the number that you want the factorial'))

numFact = numFactorial(num)

print('the factorial of the number', num, ' is ', numFact)