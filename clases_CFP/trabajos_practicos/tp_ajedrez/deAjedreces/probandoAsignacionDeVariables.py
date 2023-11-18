import random

# Crear una lista con 64 ceros
tablero = [0] * 64

# Generar tres números aleatorios distintos entre 1 y 64
numeros_aleatorios = random.sample(range(64), 3)

# Asignar valores aleatorios a las variables correspondientes
A2, B3, C1 = 14, 20, 50

# Asignar los valores aleatorios a las variables
for i, valor in enumerate(numeros_aleatorios):
    tablero[valor] = [A2, B3, C1][i]

# Imprimir el tablero resultante
for fila in range(8):
    for columna in range(8):
        indice = fila * 8 + columna
        print(f"{chr(65 + columna)}{8 - fila} = {tablero[indice]}", end=", ")
    print()
