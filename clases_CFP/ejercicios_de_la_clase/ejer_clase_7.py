# Ejercicio7. Pedir un número N, y mostrar todos los números del 1 al N.

numero_N = int(input('ingresa el numero N: \n'))
i = 0

while True:
    i += 1
    print(i)
    if i == numero_N:
        break