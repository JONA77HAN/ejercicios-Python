# Ejercicio 4
# Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, 
# los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.

loteria = []

for numero in range(6):
    numero = int(input('Ingrese el numero ganador: '))
    loteria.append(numero)
loteria.sort()
print(f'Los numeros ganadores de la loteria en orden son: {loteria}')    


