#Ejercicio1. Pedir un número y mostrar su cuadrado, repetir el proceso hasta que se introduzca un número negativo.
numA = 1
while numA >= 0:
	numA = int(input('Ingrese un numero: '))
	resultado = numA ** 2
	print('Cuadrado de '+str(numA)+' es '+str(resultado))