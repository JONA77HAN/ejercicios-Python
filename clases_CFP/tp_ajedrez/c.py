from random import randint
A8, A7, A6, A5, A4, A3, A2, A1 = 0, 0, 0, 0, 0, 0, 0, 0
B8, B7, B6, B5, B4, B3, B2, B1 = 0, 0, 0, 0, 0, 0, 0, 0 
C8, C7, C6, C5, C4, C3, C2, C1 = 0, 0, 0, 0, 0, 0, 0, 0
D8, D7, D6, D5, D4, D3, D2, D1 = 0, 0, 0, 0, 0, 0, 0, 0
E8, E7, E6, E5, E4, E3, E2, E1 = 0, 0, 0, 0, 0, 0, 0, 0
F8, F7, F6, F5, F4, F3, F2, F1 = 0, 0, 0, 0, 0, 0, 0, 0 
G8, G7, G6, G5, G4, G3, G2, G1 = 0, 0, 0, 0, 0, 0, 0, 0
H8, H7, H6, H5, H4, H3, H2, H1 = 0, 0, 0, 0, 0, 0, 0, 0
def tablero(): #funcion que define el tablero en blanco
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
# la mostramos en pantalla
tablero() 
# Define las cantidades para cada pieza  --> blancas:
peon_blanco = int(randint(0, 8))
caballo_blanco = randint(0, 2)
alfil_blanco = randint(0, 2)
torre_blanca = randint(0, 2)
reina_blanca = randint(0, 1)
rey_blanco = 1
# Negras: 
peon_negro = randint(0, 8)
caballo_negro = randint(0, 2)
alfil_negro = randint(0, 2)
torre_negra = randint(0, 2)
reina_negra = randint(0, 1)
rey_negro = 1
#Pongamos las fichas en el tablero:



# Sacando el puntaje de cada jugador: ------>
# asignamos los valores de cada pieza
puntos_de_cada_pieza = {
    '♟' : peon_blanco*1,
    '♙' : peon_negro*1,
    '♞' : caballo_blanco*3,
    '♘' : caballo_negro*3,
    '♝' : alfil_blanco*3,
    '♗' : alfil_negro*3,
    '♜' : torre_blanca*5,
    '♖' : torre_negra*5,
    '♛' : reina_blanca*9,
    '♕' : reina_negra*9,
    '♚' : rey_blanco*4,
    '♔' : rey_negro*4
}
#para corroborar el puntaje y la cantidad de piezas
print(caballo_blanco)
print(puntos_de_cada_pieza)

#calculemos los puntos de cada jugador
puntos_jugador_blancas = peon_blanco+caballo_blanco*3+alfil_blanco*3+torre_blanca*5+reina_blanca*9+rey_blanco*4
puntos_jugador_negras = peon_negro+caballo_negro*3+alfil_negro*3+torre_negra*5+reina_negra*9+rey_negro*4
print(puntos_jugador_blancas)
# Y mostremoslo en pantalla
print('el jugador de piezas blancas tiene ' + str(puntos_jugador_blancas)+' puntos')
print('Y el de piezas negras '+str(puntos_jugador_negras)+ ' puntos' )

pieces = ['♔', '♕', '♖', '♗', '♘', '♙', '♚', '♛', '♜', '♝', '♞', '♟']


# Define las variables para las posiciones de las fichas
A8, B8, C8, D8, E8, F8, G8, H8 = piezas_en_el_tablero[0:8]
A7, B7, C7, D7, E7, F7, G7, H7 = piezas_en_el_tablero[8:16]
A6, B6, C6, D6, E6, F6, G6, H6 = piezas_en_el_tablero[16:24]
A5, B5, C5, D5, E5, F5, G5, H5 = piezas_en_el_tablero[24:32]
A4, B4, C4, D4, E4, F4, G4, H4 = piezas_en_el_tablero[32:40]
A3, B3, C3, D3, E3, F3, G3, H3 = piezas_en_el_tablero[40:48]
A2, B2, C2, D2, E2, F2, G2, H2 = piezas_en_el_tablero[48:56]
A1, B1, C1, D1, E1, F1, G1, H1 = piezas_en_el_tablero[56:64]