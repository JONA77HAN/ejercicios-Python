# Ejercicio 11: 
# Leer 10 enteros, guardarlos en una lista
# Leer N y buscarlo en la lista. 
# Se debe mostrar la posición en que se encuentra. Si no está, indicarlo con un mensaje.

from random import randint
lista = []
for i in range(10):
    lista.append(randint(0,50))
print(lista)    
N = int(input('ingrese un numero: '))
if N in lista:
    posicion = lista.index(N)
    print('Está en la posicion ' + str(posicion))
else:
    print('No está')