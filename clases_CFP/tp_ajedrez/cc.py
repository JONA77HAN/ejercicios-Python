import random

# Lista de nombres a asignar aleatoriamente
nombres = ['lolo', 'juan', 'jose']

# Mezcla los nombres aleatoriamente
random.shuffle(nombres)

# Define las variables para las posiciones del tablero
A8, B8, C8, D8, E8, F8, G8, H8 = nombres[0:8]
A7, B7, C7, D7, E7, F7, G7, H7 = nombres[8:16]
A6, B6, C6, D6, E6, F6, G6, H6 = nombres[16:24]
A5, B5, C5, D5, E5, F5, G5, H5 = nombres[24:32]
A4, B4, C4, D4, E4, F4, G4, H4 = nombres[32:40]
A3, B3, C3, D3, E3, F3, G3, H3 = nombres[40:48]
A2, B2, C2, D2, E2, F2, G2, H2 = nombres[48:56]
A1, B1, C1, D1, E1, F1, G1, H1 = nombres[56:64]

# Función para imprimir el tablero
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
