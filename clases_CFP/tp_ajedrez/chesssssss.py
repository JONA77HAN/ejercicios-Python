from random import randint

# Función para inicializar el tablero
def initialize_board():
    board = [[' ' for _ in range(8)] for _ in range(8)]
    return board

# Función para mostrar el tablero
def print_board(board):
    print('     -------------------------------')
    for i in range(8):
        row = '   '.join(board[i])
        print(f'{8 - i} -{row}   {8 - i}')
    print('     -------------------------------')
    print('      A   B   C   D   E   F   G   H')

# Función para agregar piezas aleatorias al tablero
def add_random_pieces(board, pieces):
    for piece in pieces:
        while True:
            row = randint(0, 7)
            col = randint(0, 7)
            if board[row][col] == ' ':
                board[row][col] = piece
                break

# Función para calcular el puntaje de un jugador
def calculate_score(board, player):
    score = 0
    for row in board:
        for piece in row:
            if piece in piece_values:
                if piece.isupper() and player == 'Blanco':
                    score += piece_values[piece]
                elif piece.islower() and player == 'Negro':
                    score += piece_values[piece]
    return score

# Función para verificar si hay jaque
def is_check(board, player):
    king = '♚' if player == 'Negro' else '♔'
    king_pos = None

    for i in range(8):
        for j in range(8):
            if board[i][j] == king:
                king_pos = (i, j)

    for i in range(8):
        for j in range(8):
            piece = board[i][j]
            if piece in piece_values and (piece.islower() if player == 'Negro' else piece.isupper()):
                if is_threatening(piece, (i, j), king_pos):
                    return True
    return False

# Función para verificar si una pieza amenaza al rey
def is_threatening(piece, piece_pos, king_pos):
    dx = abs(piece_pos[0] - king_pos[0])
    dy = abs(piece_pos[1] - king_pos[1])
    return (piece in piece_moves) and (dx, dy) in piece_moves[piece]

# Define las piezas y sus valores
piece_values = {
    '♟': 1, '♞': 3, '♝': 3, '♜': 5, '♛': 9, '♚': 4,
    '♙': 1, '♘': 3, '♗': 3, '♖': 5, '♕': 9, '♔': 4
}

# Define los movimientos válidos para cada pieza
piece_moves = {
    '♟': [(1, 0)],
    '♞': [(1, 2), (2, 1)],
    '♝': [(1, 1)],
    '♜': [(1, 0), (0, 1)],
    '♛': [(1, 1), (1, 0), (0, 1)],
    '♚': [(1, 1), (1, 0), (0, 1)],
    '♙': [(-1, 0)],
    '♘': [(1, 2), (2, 1)],
    '♗': [(1, 1)],
    '♖': [(1, 0), (0, 1)],
    '♕': [(1, 1), (1, 0), (0, 1)],
    '♔': [(1, 1), (1, 0), (0, 1)]
}

# Inicializa el tablero
board = initialize_board()

# Agrega piezas aleatorias para el jugador blanco
white_pieces = ['♙'] * randint(0, 8) + ['♘'] * randint(0, 2) + ['♗'] * randint(0, 2) + ['♖'] * randint(0, 2) + ['♕'] * randint(0, 1) + ['♔']
add_random_pieces(board, white_pieces)

# Agrega piezas aleatorias para el jugador negro
black_pieces = ['♟'] * randint(0, 8) + ['♞'] * randint(0, 2) + ['♝'] * randint(0, 2) + ['♜'] * randint(0, 2) + ['♛'] * randint(0, 1) + ['♚']
add_random_pieces(board, black_pieces)

# Imprime el tablero con las piezas
print_board(board)

# Calcula y muestra el puntaje de cada jugador
score_white = calculate_score(board, 'Blanco')
score_black = calculate_score(board, 'Negro')
print(f'Puntaje del jugador Blanco: {score_white}')
print(f'Puntaje del jugador Negro: {score_black}')

# Verifica si hay jaque
if is_check(board, 'Blanco'):
    print('¡Jaque al jugador Blanco!')
if is_check(board, 'Negro'):
    print('¡Jaque al jugador Negro!')
