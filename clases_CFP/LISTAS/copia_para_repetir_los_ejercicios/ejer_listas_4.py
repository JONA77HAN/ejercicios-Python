# Ejercicio 4: 
# Leer 10 números enteros y guardarlos en una lista. 
# Debemos mostrarlos en el siguiente orden: 
# el primero, el último, el segundo, el penúltimo, el tercero, el ante-penúltimo, etc.
# spam.insert(posicion,valor)

from random import randint
listaNum = []
listaNumInversa = []
c = 0
for i in range(10):
	c += 1
	num = randint(1,20)
	print(str(c) + ' --> Numero: '+str(num))
	listaNum.append(num + c)
print(listaNum)
# Asi puedo llamar al ultimo lugar, al ultimo valor de la lista
print('-'*25)
for i in range(5):
	print(listaNum[i])
	print(listaNum[-1-i])
	print('-'*25)

