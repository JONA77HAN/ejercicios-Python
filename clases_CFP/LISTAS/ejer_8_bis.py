#Ejercicio7.  Leer mediante el teclado 8 números. Después se debe pedir un número y una posición, insertarlo en la posición indicada, desplazando hacia la derecha las posiciones que le siguen.

#Ejercicio8.  Crear un programa que lea por teclado una lista de 10 números enteros y la desplace una posición hacia abajo/la derecha, manteniendo la misma cantidad de posiciones: el primero pasa a ser el segundo, el segundo pasa a ser el tercero y así sucesivamente. El último pasa a ser el primero.

#Resuelve: Herrera
from random import randint
from misFunciones import limpiarPantalla
from time import sleep
listaNum = []
for i in range(10):
	num = randint(1,200)
	print('Numero: '+str(num))
	listaNum.append(num)
print(listaNum)
while True:
	limpiarPantalla()
	listaNum.insert(0,listaNum[9])
	del listaNum[10]
	print(listaNum)
	sleep(1)
	
