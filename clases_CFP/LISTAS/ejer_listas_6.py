# Ejercicio 6: 
# Leer por teclado una serie de 10 números enteros. 
# La aplicación debe indicarnos si los números:  
# están ordenados de forma creciente, decreciente, o si están desordenados.

# [2,3,4,5,6,7,8,9,10,11] ->Ordenada Creciente
# [5,4,3,2,1,1,1,1,1,1] ->Ordenada Decreciente
# [1,3,5,8,6,4,9,20,1] ->Desordenada

from random import randint

lista = []
"""
for i in range(10):
    num = randint(1,10)
    lista.append(num)
print(lista)    
"""
for i in range(10):
    num = int(input('ingresar numeros: '))
    lista.append(num)

if lista[0] < lista[1] < lista[2] < lista[3] < lista[4] < lista[5] < lista[6] < lista[7] < lista[8] < lista[9]:
    print('numeros ingresados de forma ascendente')
elif lista[0] > lista[1] > lista[2] > lista[3] > lista[4] > lista[5] > lista[6] > lista[7] > lista[8] > lista[9]:
    print('numeros ingresados de forma descendente')    
else:
    print('numeros ingresados de forma desordenada')
