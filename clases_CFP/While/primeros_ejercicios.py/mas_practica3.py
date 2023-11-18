# Ejercicio12. 
# Pedir 10 números. 
# Mostrar el promedio de los números positivos, 
# El promedio de los números negativos 
# Y la cantidad de ceros.

from random import randint

negsuma=0
negcontador=0
possuma=0
poscontador=0
cerocontador=0

for n in range(10):
	numero = randint(-5,5)#int(input('ingrese numero: '))
	print('Numero: '+str(numero))
	if numero < 0:
		negsuma += numero
		negcontador += 1
	elif numero > 0:
		possuma += numero
		poscontador += 1
	else:
		cerocontador += 1

if negcontador > 0:
	promNeg = round(negsuma/negcontador,2)
	print('El promedio de los numeros negativos es '+str(promNeg))
else:
	print('No se ingresaron negativos.')
if poscontador > 0:
	promPos = round(possuma/poscontador,2)
	print('el promedio de los numeros positivos es '+str(promPos))
else:
	print('No se ingresaron positivos.')
print('la cantidad de ceros ingresados es '+str(cerocontador))
