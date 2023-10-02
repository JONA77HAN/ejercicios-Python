# Ejercicio 6: 
# Leer por teclado una serie de 5 números enteros. 
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

for i in range(len(lista)-1):
    if lista[1] > lista[i + 1]:
        descendente = True
    elif lista[i] < lista[i +1]:
        ascendente = True
    else:
        desordenada = True

if ascendente == True:
    print('numeros ingresados de forma ascendente')
elif descendente == True:
    print('numeros ingresados de forma descendente')
else:
    print('numeros ingresados de forma desordenada')        