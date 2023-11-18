#Ejercicio9. Pedir 15 números y escribir la suma total. (Usando ciclo FOR)

#Resuelve: Gianelli
from random import randint

sum = 0

for i in range(1,16):
	num = randint(1,10)  #int(input('Ingrese 15 numeros  : \n'))
	print(str(i)+': '+str(num))
	sum = sum + num  #sum += num
print('la suma total de todos los numeros es: ' + str(sum))