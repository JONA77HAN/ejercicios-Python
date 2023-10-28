import random

# Define the piece values
piece_values = {
    'pawn': 1,
    'knight': 3,
    'bishop': 3,
    'rook': 5,
    'queen': 9,
    'king': 4,
}

# Generate random piece counts for white and black
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

# Calculate the scores for white and black
white_score = sum(white_pieces[piece] * piece_values[piece] for piece in white_pieces)
black_score = sum(black_pieces[piece] * piece_values[piece] for piece in black_pieces)

# Check if a king is adjacent to any opposing piece
is_adjacent = False
if white_pieces['king'] == 1 and black_pieces['king'] == 1:
    is_adjacent = True

# Print the results
print("White Pieces:", white_pieces)
print("Black Pieces:", black_pieces)
print("White Score:", white_score)
print("Black Score:", black_score)
if is_adjacent:
    print("A king is adjacent to an opposing piece.")
