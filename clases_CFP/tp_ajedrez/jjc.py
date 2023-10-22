import random

# Define las posiciones del tablero como cadenas
posiciones = ["A8", "B8", "C8", "D8", "E8", "F8", "G8", "H8",
              "A7", "B7", "C7", "D7", "E7", "F7", "G7", "H7",
              "A6", "B6", "C6", "D6", "E6", "F6", "G6", "H6",
              "A5", "B5", "C5", "D5", "E5", "F5", "G5", "H5",
              "A4", "B4", "C4", "D4", "E4", "F4", "G4", "H4",
              "A3", "B3", "C3", "D3", "E3", "F3", "G3", "H3",
              "A2", "B2", "C2", "D2", "E2", "F2", "G2", "H2",
              "A1", "B1", "C1", "D1", "E1", "F1", "G1", "H1"]

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
piezas_en_el_tablero = (
    peon_blanco + caballo_blanco + alfil_blanco + torre_blanca + reina_blanca + rey_blanco +
    peon_negro + caballo_negro + alfil_negro + torre_negra + reina_negra + rey_negro
)

# Selecciona aleatoriamente las posiciones en el tablero para las piezas
donde_iran_las_piezas = random.sample(posiciones, len(piezas_en_el_tablero))

# Asignar las piezas aleatorias a las posiciones
for i in range(len(piezas_en_el_tablero)):
    posiciones[posiciones.index(donde_iran_las_piezas[i])] = piezas_en_el_tablero[i]

# Función para imprimir el tablero con piezas
def tablero():
    print('     -------------------------------')
    print('8 -   ' + '   '.join(posiciones[0:8]))
    print('7 -   ' + '   '.join(posiciones[8:16]))
    print('6 -   ' + '   '.join(posiciones[16:24]))
    print('5 -   ' + '   '.join(posiciones[24:32]))
    print('4 -   ' + '   '.join(posiciones[32:40]))
    print('3 -   ' + '   '.join(posiciones[40:48]))
    print('2 -   ' + '   '.join(posiciones[48:56]))
    print('1 -   ' + '   '.join(posiciones[56:64]))
    print('     -------------------------------')
    print('      A   B   C   D   E   F   G   H')

tablero()
