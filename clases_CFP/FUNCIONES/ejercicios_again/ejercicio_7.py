# Ejercicio7. Diseña una función que decida si un número es primo.
# Aclaraciones:
# Es primo si tiene solo 2 divisores (1 y si mismo)
# Un numero es divisor de otro si el modulo/resto les da 0.

# Ejemplo:
# Le paso 5
# Devuelve "Es primo"/True
# Le paso 8
# Devuelve "No es primo"/False

def primo (n) :
	for i in range(2,n):#2,3,4,5,6,7,8,9
		if n % i == 0:
			return False 
	return True
n=int(input('Ingrese: \n '))
if primo(n):
	print('El numero es primo')
else:
	print('El numero no es primo')


