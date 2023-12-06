# Ejercicio 3
# Escribir un programa que pida al usuario un número entero positivo y 
# muestre por pantalla todos los números impares desde 1 hasta ese número 
# separados por comas.

# Numeros impares
N = int(input('ingrese un numero entero y positivo: '))
for i in range(1, N+1, 2):
    print(i, end=', ')
    continue
# Numeros pares
n = int(input('Ingrese un numero enteo y positivo: '))
for i in range(0, n+1, 2):
    print(i, end=', ')   