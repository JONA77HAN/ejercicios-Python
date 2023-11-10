#Ejercicio3. Escribir un programa que lea una cadena y devuelva un diccionario con la cantidad de veces que aparece cada carácter en la cadena.

#Ejemplo:
#Ingreso casa
#muestro {'c':1,'a':2,'s':1}

def cantidad_letras(cadena):
	caracter= {}
	for c in cadena:
		if c in caracter:
			caracter[c] += 1
		else:
			caracter[c] = 1
		#caracter[c] = caracter.get(c,0) + 1
	return caracter

cadena = input('ingrese cadena ')
caracter = cantidad_letras(cadena)
print(caracter)
