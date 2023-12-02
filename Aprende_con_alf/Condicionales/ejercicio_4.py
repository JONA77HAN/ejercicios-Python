# Ejercicio 4
# Escribir un programa que pida al usuario un número entero y muestre 
# por pantalla si es par o impar.

numero = int(input('Ingrese un numero entero y te diré si es par o impar: '))
if numero % 2 == 0:
    print('El numero es Par')
else:
    print('El numero es Impar')