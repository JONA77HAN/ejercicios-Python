#Ejercicio2. Leer 5 números, guardarlos en una lista y mostrarlos en orden inverso al introducido.
from random import randint

lista = []
lista_inversa = []

print('Generamos una lista de cinco números aleatorios entre -50 y 50:')

for i in range(5):
	num = randint(-50,50)
	lista.append(num)

print(lista)
print('Ahora, esta lista se invertirá: ')

lista.reverse()
print(lista)

#falta invertir la lista en una nueva lista, la 'inversa'