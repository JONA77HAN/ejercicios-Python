# Ejercicio 6: 
# Leer por teclado una serie de 5 números enteros. 
# La aplicación debe indicarnos si los números:  
# están ordenados de forma creciente, decreciente, o si están desordenados.

# [2,3,4,5,6,7,8,9,10,11] ->Ordenada Creciente
# [5,4,3,2,1,1,1,1,1,1] ->Ordenada Decreciente
# [1,3,5,8,6,4,9,20,1] ->Desordenada
from random import randint
numeros = []
for i in range(5):
    numero = int(input('ingrese un numero: ')) #randint(1,3)
    numeros.append(numero)
print(numeros)    

creciente = True
for i in range(1, len(numeros)):
    if numeros[i] < numeros[i - 1]:
        creciente = False
        break

decreciente = True
for i in range(1, len(numeros)):
    if numeros[i] > numeros[i - 1]:
        decreciente = False
        break

if creciente:
    print('creciente')
elif decreciente:
    print('decreciente')
else:
    print('desordenados')



