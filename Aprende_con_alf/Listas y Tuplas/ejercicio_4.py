# Ejercicio 4
# Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, 
# los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.

numeros_ganadores = []
numero = ''

for numero in numeros_ganadores:
    numero = int(input('ingrese el numero ganador: '))
    numeros_ganadores.append(numero)
    print(numeros_ganadores)

ordenados = numeros_ganadores.sort()

print(ordenados)