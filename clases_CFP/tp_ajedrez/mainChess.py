import random
from random import randint
# Define las cantidades para cada pieza 
# Transformando los numeros numeros en piezas  --> 
# blancas:
peon_blanco = int(randint(0, 8))*'♟'
caballo_blanco = int(randint(0, 2))*'♞' 
alfil_blanco = int(randint(0, 2))*'♝'
torre_blanca = int(randint(0, 2))*'♜'
reina_blanca = int(randint(0, 1))*'♛'
rey_blanco = 1*'♚'
# Negras: 
peon_negro = int(randint(0, 8))*'♙' 
caballo_negro = int(randint(0, 2))*'♘'
alfil_negro = int(randint(0, 2))*'♗'
torre_negra = int(randint(0, 2))*'♖'
reina_negra = int(randint(0, 1))* '♕'
rey_negro = 1*'♔'
# Piezas que habrá en el tablero
piezas_en_el_tablero = [
    peon_blanco + caballo_blanco + alfil_blanco + torre_blanca + reina_blanca + rey_blanco + peon_negro
     + caballo_negro + alfil_negro + torre_negra + reina_negra + rey_negro
]
print(piezas_en_el_tablero)
# Mezcla los nombres aleatoriamente
random.shuffle(piezas_en_el_tablero)

# Define las variables para las posiciones de las fichas
A8, B8, C8, D8, E8, F8, G8, H8 = 0,0,0,0,0,0,0,0
A7, B7, C7, D7, E7, F7, G7, H7 = 0,0,0,0,0,0,0,0 
A6, B6, C6, D6, E6, F6, G6, H6 = 0,0,0,0,0,0,0,0
A5, B5, C5, D5, E5, F5, G5, H5 = 0,0,0,0,0,0,0,0
A4, B4, C4, D4, E4, F4, G4, H4 = 0,0,0,0,0,0,0,0
A3, B3, C3, D3, E3, F3, G3, H3 = 0,0,0,0,0,0,0,0
A2, B2, C2, D2, E2, F2, G2, H2 = 0,0,0,0,0,0,0,0 
A1, B1, C1, D1, E1, F1, G1, H1 = 0,0,0,0,0,0,0,0

# Función para imprimir el tablero, y poner las fichas random en el tablero
def tablero():
    print('     -------------------------------')
    print('8 -   '+ str(A8) +'   '+ str(B8) +'   '+ str(C8) +'   '+ str(D8) +'   '+ str(E8) +'   '+ str(F8) +'   '+ str(G8) +'   '+ str(H8))
    print('7 -   '+ str(A7) +'   '+ str(B7) +'   '+ str(C7) +'   '+ str(D7) +'   '+ str(E7) +'   '+ str(F7) +'   '+ str(G7) +'   '+ str(H7))
    print('6 -   '+ str(A6) +'   '+ str(B6) +'   '+ str(C6) +'   '+ str(D6) +'   '+ str(E6) +'   '+ str(F6) +'   '+ str(G6) +'   '+ str(H6))
    print('5 -   '+ str(A5) +'   '+ str(B5) +'   '+ str(C5) +'   '+ str(D5) +'   '+ str(E5) +'   '+ str(F5) +'   '+ str(G5) +'   '+ str(H5))
    print('4 -   '+ str(A4) +'   '+ str(B4) +'   '+ str(C4) +'   '+ str(D4) +'   '+ str(E4) +'   '+ str(F4) +'   '+ str(G4) +'   '+ str(H4))
    print('3 -   '+ str(A3) +'   '+ str(B3) +'   '+ str(C3) +'   '+ str(D3) +'   '+ str(E3) +'   '+ str(F3) +'   '+ str(G3) +'   '+ str(H3))
    print('2 -   '+ str(A2) +'   '+ str(B2) +'   '+ str(C2) +'   '+ str(D2) +'   '+ str(E2) +'   '+ str(F2) +'   '+ str(G2) +'   '+ str(H2))
    print('1 -   '+ str(A1) +'   '+ str(B1) +'   '+ str(C1) +'   '+ str(D1) +'   '+ str(E1) +'   '+ str(F1) +'   '+ str(G1) +'   '+ str(H1))
    print('     -------------------------------')
    print('      A   B   C   D   E   F   G   H')
# Llama a la función para imprimir el tablero
tablero()
# Armar una lista con las posiciones en las q podrian ir cada una de las piezas
lugares_en_el_tablero =  [ 
A8, B8, C8, D8, E8, F8, G8, H8, 
A7, B7, C7, D7, E7, F7, G7, H7, 
A6, B6, C6, D6, E6, F6, G6, H6, 
A5, B5, C5, D5, E5, F5, G5, H5, 
A4, B4, C4, D4, E4, F4, G4, H4, 
A3, B3, C3, D3, E3, F3, G3, H3, 
A2, B2, C2, D2, E2, F2, G2, H2, 
A1, B1, C1, D1, E1, F1, G1, H1, 
]# Hacer una lista con el contenido de los A1, A2 etc
print(lugares_en_el_tablero)

# Mezcla las piezas aleatoriamente
random.shuffle(piezas_en_el_tablero)

# Itera a través de las variables de posición y asigna las piezas aleatorias
for i in range(len(lugares_en_el_tablero)):
    lugares_en_el_tablero[i] = piezas_en_el_tablero[i]

# Llama a la función para imprimir el tablero con las piezas asignadas aleatoriamente
tablero()
