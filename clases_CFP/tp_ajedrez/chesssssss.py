import random

# Define las cantidades para cada pieza
# Transformando los números en piezas
# Blancas:
peon_blanco = ['♟'] * random.randint(0, 8)
caballo_blanco = ['♞'] * random.randint(0, 2)
alfil_blanco = ['♝'] * random.randint(0, 2)
torre_blanca = ['♜'] * random.randint(0, 2)
reina_blanca = ['♛'] * random.randint(0, 1)
rey_blanco = ['♚']

# Negras:
peon_negro = ['♙'] * random.randint(0, 8)
caballo_negro = ['♘'] * random.randint(0, 2)
alfil_negro = ['♗'] * random.randint(0, 2)
torre_negra = ['♖'] * random.randint(0, 2)
reina_negra = ['♕'] * random.randint(0, 1)
rey_negro = ['♔']

# Piezas que habrá en el tablero
piezas_en_el_tablero = (
    peon_blanco + caballo_blanco + alfil_blanco + torre_blanca + reina_blanca + rey_blanco +
    peon_negro + caballo_negro + alfil_negro + torre_negra + reina_negra + rey_negro
)

# Mezcla las piezas aleatoriamente
random.shuffle(piezas_en_el_tablero)

# Define el tablero como una lista 2D
tablero = [[' '] * 8 for _ in range(8)]

# Llena el tablero con las piezas
for i in range(8):
    for j in range(8):
        tablero[i][j] = piezas_en_el_tablero.pop(0)

# Función para imprimir el tablero con las fichas asignadas
def imprimir_tablero():
    print('     -------------------------------')
    for i in range(8):
        fila = ' '.join(tablero[i])
        print(f'{8 - i} -   {fila}')
    print('     -------------------------------')
    print('      A   B   C   D   E   F   G   H')

# Llama a la función para imprimir el tablero
imprimir_tablero()
