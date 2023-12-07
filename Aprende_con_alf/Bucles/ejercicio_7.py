# Ejercicio 7
# Escribir un programa que muestre por pantalla la tabla de multiplicar 
# del 1 al 10.

#primero elige la tabla q quieres
n = int(input('Ingresa tu numero: '))

for i in range(1, 11, 1):
    print(f'{i} x {n} = {i*n}')