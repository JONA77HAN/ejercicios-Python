# Ejercicio 4
# Escribir un programa que pida al usuario un número entero positivo y 
# muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.

N = int(input('Ingrese un numero: '))
for i in range(N, -1, -1):
    print(i, end=', ')