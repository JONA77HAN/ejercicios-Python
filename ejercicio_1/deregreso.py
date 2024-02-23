# Ejercicio 1: Suma de dos números
# Escribe un programa que solicite al usuario dos números enteros y luego muestre la suma de esos dos números.

num_a = int(input('ingrese un numero para sumar: '))
num_b = int(input(f'Ingresaste el numero {num_a} ahora ingresa otro numero: '))
resultado = num_a + num_b
print(f'El resultado de la suma es {resultado}')