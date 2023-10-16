#Si deseas posicionar piezas de ajedrez de forma aleatoria 
# en este tablero vacío, puedes hacerlo de la siguiente manera 
# utilizando el módulo randint de Python:
from random import randint

# Crear el tablero vacío
board = [[' ' for _ in range(8)] for _ in range(8)]

# Lista de piezas de ajedrez
pieces = ['♔', '♕', '♖', '♗', '♘', '♙', '♚', '♛', '♜', '♝', '♞', '♟']

# Coloca piezas aleatoriamente en el tablero
for piece in pieces:
    while True:
        row = randint(0, 7)
        col = randint(0, 7)
        if board[row][col] == ' ':
            board[row][col] = piece
            break

# Imprime el tablero
print('     -------------------------------')
for i in range(8):
    print(f'{8 - i} -   ' + '   '.join(board[i]) + '   ' + str(8 - i))
print('     -------------------------------')
print('      A   B   C   D   E   F   G   H')
