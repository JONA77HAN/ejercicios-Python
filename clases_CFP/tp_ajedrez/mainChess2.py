import random

# Define los lugares en el tablero
lugares_en_el_tablero = [
    'A8', 'B8', 'C8', 'D8', 'E8', 'F8', 'G8', 'H8',
    'A7', 'B7', 'C7', 'D7', 'E7', 'F7', 'G7', 'H7',
    'A6', 'B6', 'C6', 'D6', 'E6', 'F6', 'G6', 'H6',
    'A5', 'B5', 'C5', 'D5', 'E5', 'F5', 'G5', 'H5',
    'A4', 'B4', 'C4', 'D4', 'E4', 'F4', 'G4', 'H4',
    'A3', 'B3', 'C3', 'D3', 'E3', 'F3', 'G3', 'H3',
    'A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2',
    'A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1',
]

# Crea el tablero vacío con lugares marcados como vacíos (' ')
tablero = [' '] * len(lugares_en_el_tablero)

# Elige aleatoriamente la cantidad de piezas que deseas colocar (por ejemplo, 10 piezas)
cantidad_piezas = 10

# Elige aleatoriamente las posiciones donde colocarás las piezas
posiciones_piezas = random.sample(lugares_en_el_tablero, cantidad_piezas)

# Define las piezas que deseas colocar
piezas = ['♟', '♞', '♝', '♜', '♛', '♚']

# Asigna aleatoriamente las piezas a las posiciones seleccionadas
for posicion in posiciones_piezas:
    tablero[lugares_en_el_tablero.index(posicion)] = random.choice(piezas)

# Muestra el tablero resultante
for i in range(8):
    fila = ' '.join(tablero[i * 8:i * 8 + 8])
    print(f'{8 - i} -   {fila}')
