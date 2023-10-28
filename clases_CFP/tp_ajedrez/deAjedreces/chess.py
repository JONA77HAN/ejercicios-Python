from random import randint, choice

# Inicializa el tablero vacío
chess_board = [[' ' for _ in range(8)] for _ in range(8)]

# Define las piezas y sus valores
pieces = ['♔', '♕', '♖', '♗', '♘', '♙', '♚', '♛', '♜', '♝', '♞', '♟']
piece_values = {
    '♔': 4, '♕': 9, '♖': 5, '♗': 3, '♘': 3, '♙': 1,
    '♚': -4, '♛': -9, '♜': -5, '♝': -3, '♞': -3, '♟': -1
}

# Genera cantidades aleatorias de piezas
peones = randint(0, 8)
caballos = randint(0, 2)
alfiles = randint(0, 2)
torres = randint(0, 2)
reina = randint(0, 1)
rey = 1

# Combina las piezas en una lista
pieces_list = ['♙'] * peones + ['♘'] * caballos + ['♗'] * alfiles + ['♖'] * torres + ['♕'] * reina + ['♔'] * rey

# Coloca piezas aleatoriamente en el tablero
for piece in pieces_list:
    while True:
        row = randint(0, 7)
        col = randint(0, 7)
        if chess_board[row][col] == ' ':
            chess_board[row][col] = piece
            break

# Imprime el tablero con las piezas
print('     -------------------------------')
for i in range(8):
    row_str = f'{8 - i} -   ' + '   '.join(chess_board[i]) + '   ' + str(8 - i)
    print(row_str)
print('     -------------------------------')
print('      A   B   C   D   E   F   G   H')

# Calcula el puntaje de cada jugador
score_white = sum(piece_values[piece] for row in chess_board for piece in row if piece in piece_values and piece.isupper())
score_black = sum(piece_values[piece] for row in chess_board for piece in row if piece in piece_values and piece.islower())

print(f'Puntaje del jugador blanco: {score_white}')
print(f'Puntaje del jugador negro: {score_black}')
