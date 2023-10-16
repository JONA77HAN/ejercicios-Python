# Ejercicio 11: 
# Leer 10 enteros, guardarlos en una lista
# Leer N y buscarlo en la lista. 
# Se debe mostrar la posición en que se encuentra. Si no está, indicarlo con un mensaje.
from random import randint
lista = []
for i in range(10):
    lista.append(randint(0,100))
print(lista)
# En este caso hicimos q muestre la posicion
posicion = int(input('Ingrese el numero de lista que quiere ver: '))
print(lista[posicion])    
# Si quiero saber si el numero esta o no en la lista
N = int(input('ingrese el numero q busca: '))
if N in lista:
    posicion = lista.index(N)
    print('Esta en la posicion ' + str(posicion))
else:
    print('No esta')