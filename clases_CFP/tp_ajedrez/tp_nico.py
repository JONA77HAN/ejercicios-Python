import random

# Tamaño del tablero (8x8 para ajedrez)
filas = 8
columnas = 8

# Crear un tablero vacío
tablero = [['  ' for _ in range(columnas)] for _ in range(filas)]

# Definir las piezas y sus cantidades
piezas_blancas = {
    'Peon': random.randint(0, 8),
    'Caballo': random.randint(0, 2),
    'Alfil': random.randint(0, 2),
    'Torre': random.randint(0, 2),
    'Reina': random.randint(0, 1),
    'Rey': 1
}

piezas_negras = {
    'Peon': random.randint(0, 8),
    'Caballo': random.randint(0, 2),
    'Alfil': random.randint(0, 2),
    'Torre': random.randint(0, 2),
    'Reina': random.randint(0, 1),
    'Rey': 1
}

# Definir los valores de las piezas
valores_piezas = {
    'Peon': 1,
    'Caballo': 3,
    'Alfil': 3,
    'Torre': 5,
    'Reina': 9,
    'Rey': 4
}

# Colocar piezas aleatorias en el tablero para las blancas
for nombre_pieza in piezas_blancas:
    cantidad = piezas_blancas[nombre_pieza]
    for _ in range(cantidad):
        while True:
            fila = random.randint(0, filas - 1)
            columna = random.randint(0, columnas - 1)
            if tablero[fila][columna] == '  ':
                tablero[fila][columna] = 'B' + nombre_pieza[0]  # Usamos dos letras (PB) para piezas blancas
                break

# Colocar piezas aleatorias en el tablero para las negras
for nombre_pieza in piezas_negras:
    cantidad = piezas_negras[nombre_pieza]
    for _ in range(cantidad):
        while True:
            fila = random.randint(0, filas - 1)
            columna = random.randint(0, columnas - 1)
            if tablero[fila][columna] == '  ':
                tablero[fila][columna] = 'N' + nombre_pieza[0]  # Usamos dos letras (PN) para piezas negras
                break

# Mostrar el tablero
for i in range(filas):
    for j in range(columnas):
        print(f'|{tablero[i][j]}', end='')
    print('|')
    if i != filas - 0:
        print('+' + '--' * columnas + '-------+')

# Sumar los puntos de las piezas blancas
puntos_blancas = sum(valores_piezas[pieza] * piezas_blancas[pieza] for pieza in piezas_blancas)

# Sumar los puntos de las piezas negras
puntos_negras = sum(valores_piezas[pieza] * piezas_negras[pieza] for pieza in piezas_negras)

# Determinar el ganador
if puntos_blancas > puntos_negras:
    ganador = "Blancas"
elif puntos_negras > puntos_blancas:
    ganador = "Negras"
else:
    ganador = "Empate"

# Mostrar el resultado
print(f"Puntos de las piezas blancas: {puntos_blancas}")
print(f"Puntos de las piezas negras: {puntos_negras}")
print(f"El ganador es: {ganador}")
