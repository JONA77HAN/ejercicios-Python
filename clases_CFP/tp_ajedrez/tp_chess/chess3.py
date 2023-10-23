import random

# Define the chess piece Unicode characters and their values
piece_symbols = {
    'pawn': '♟',
    'knight': '♞',
    'bishop': '♝',
    'rook': '♜',
    'queen': '♛',
    'king': '♚',
}

piece_values = {
    'pawn': 1,
    'knight': 3,
    'bishop': 3,
    'rook': 5,
    'queen': 9,
    'king': 4,
}

# Initialize the chess board as an 8x8 matrix with empty squares
chess_board = [[' ' for _ in range(8)] for _ in range(8)]

# Generate random piece counts for both white and black players
white_pieces = {
    'pawn': random.randint(0, 8),
    'knight': random.randint(0, 2),
    'bishop': random.randint(0, 2),
    'rook': random.randint(0, 2),
    'queen': random.randint(0, 1),
    'king': 1,
}

black_pieces = {
    'pawn': random.randint(0, 8),
    'knight': random.randint(0, 2),
    'bishop': random.randint(0, 2),
    'rook': random.randint(0, 2),
    'queen': random.randint(0, 1),
    'king': 1,
}

# Place white pieces on the board
for piece, count in white_pieces.items():
    for _ in range(count):
        while True:
            row, col = random.randint(0, 7), random.randint(0, 7)
            if chess_board[row][col] == ' ':
                chess_board[row][col] = piece_symbols[piece]
                break

# Place black pieces on the board
for piece, count in black_pieces.items():
    for _ in range(count):
        while True:
            row, col = random.randint(0, 7), random.randint(0, 7)
            if chess_board[row][col] == ' ':
                chess_board[row][col] = piece_symbols[piece]
                break

# Calculate the score for each player
white_score = sum(piece_values[piece] for row in chess_board for piece in row if piece in piece_symbols)
black_score = sum(piece_values[piece] for row in chess_board for piece in row if piece in piece_symbols)

# Check if a king is adjacent to any piece of the opposite team
king_positions = {'white': None, 'black': None}
for row in range(8):
    for col in range(8):
        if chess_board[row][col] == piece_symbols['king']:
            if row > 0 and chess_board[row - 1][col] != ' ':
                king_positions['white'] = (row, col)
            if row < 7 and chess_board[row + 1][col] != ' ':
                king_positions['black'] = (row, col)

# Print the board, scores, and king positions
for row in chess_board:
    print(' '.join(row))
print("White Score:", white_score)
print("Black Score:", black_score)
print("King Positions:", king_positions)
