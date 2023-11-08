#Ejercicio3. Ídem una versión que calcule el máximo de 3 números.

def maximo(a,b,c):
	if a > b and a > c:
		print ('el numero maximo es ' + str(a))
	elif b > c and b > a:
		print ('el numero maximo es ' + str(b))
	else:
		print ('el numero maximo es ' + str(c))
a = int(input('ingrese el numero a : '))
b = int(input('ingrese el numero b : '))
c = int(input('ingrese el numero c : '))
maximo(a,b,c)        
   