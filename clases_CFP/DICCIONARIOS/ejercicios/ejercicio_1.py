#Ejercicio1.  Escribir un programa que pida un número por teclado y que cree un diccionario cuyas claves sean desde el número 1 hasta el número indicado, y los valores sean los cuadrados de las claves.

#Pedir un numero, N
#Crear un diccionario
#Sus claves van desde 1 hasta la N.
#Y los valores de cada clave es la clave al cuadrado.

N = int(input('Ingrese un numero: '))
dicEj = {}
for i in range(1,N+1):
	dicEj[i] = i ** 2
print(dicEj)