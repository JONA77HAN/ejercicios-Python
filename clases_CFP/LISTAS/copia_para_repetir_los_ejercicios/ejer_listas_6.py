from random import randint

lista = []
orden = ''

for i in range(3):
    num = randint(0, 3)  # Cambia el rango según tus necesidades
    lista.append(num)

print(lista)

creciente = decreciente = True  # Inicialmente, asumimos que la lista está ordenada

for i in range(len(lista) - 1):
    if lista[i] > lista[i + 1]:
        decreciente = False
    elif lista[i] < lista[i + 1]:
        creciente = False

# Comprobamos el estado de ordenación
if creciente:
    orden = 'creciente'
elif decreciente:
    orden = 'decreciente'
else:
    orden = 'desordenada'

print('La lista quedó de forma ' + orden + '.')
