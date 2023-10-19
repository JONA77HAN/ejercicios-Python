import random

# Define las piezas de ajedrez
piezas = [
    '♟', '♞', '♝', '♜', '♛', '♚',
    '♙', '♘', '♗', '♖', '♕', '♔',
]

# Mezcla las piezas aleatoriamente
random.shuffle(piezas)

# Crea un tablero vacío representado como un diccionario
tablero = {}
for letra in 'ABCDEFGH':
    for numero in '12345678':
        casilla = letra + numero
        tablero[casilla] = ' '

# Llena el tablero con las piezas aleatorias
for casilla in tablero:
    if tablero[casilla] == ' ' and piezas:
        pieza = piezas.pop()
        tablero[casilla] = pieza

# Función para imprimir el tablero
def imprimir_tablero(tablero):
    for numero in '87654321':
        fila = ''.join(tablero[letra + numero] for letra in 'ABCDEFGH')
        print(numero + ' | ' + fila + ' |')
    print('   -------------------')
    print('    A B C D E F G H')

# Imprime el tablero
imprimir_tablero(tablero)
