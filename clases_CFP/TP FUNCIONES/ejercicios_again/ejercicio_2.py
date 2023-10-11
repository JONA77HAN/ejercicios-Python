#Ejercicio2. Diseñar una función que tenga como parámetros dos números, y que calcule el máximo
def maximo(j, k):
    if j > k: 
        print(f'{j} es el máximo de los numeros ingresados')
    else:
        print(f'{k} es el máximo numero ingresado')
M = int(input('ingrese numero: ')) 
N = int(input('ingrese numero: '))
maximo(M, N)            
