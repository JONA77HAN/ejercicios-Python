def tablero_1(tablero):
    print('TA TE TI')
    print(tablero[0] + '  /  ' + tablero[1] + '  /  ' + tablero[2])
    print('-'*15)
    print(tablero[3] + '  /  ' + tablero[4] + '  /  ' + tablero[5])
    print('-'*15)
    print(tablero[6] + '  /  ' + tablero[7] + '  /  ' + tablero[8])

def verificar_ganador(tablero, jugador):
    combinaciones_ganadoras = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Filas
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columnas
        [0, 4, 8], [2, 4, 6]  # Diagonales
    ]

    for combinacion in combinaciones_ganadoras:
        a, b, c = combinacion
        if tablero[a] == tablero[b] == tablero[c] == jugador:
            return True
    return False

tablero = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
jugador_actual = 'X'
turno = 1

while True:
    tablero_1(tablero)
    eleccion = int(input(f'Jugador "{jugador_actual}", ingrese su posición: '))

    if 1 <= eleccion <= 9 and tablero[eleccion - 1] not in ['X', 'O']:
        tablero[eleccion - 1] = jugador_actual
    else:
        print('Movimiento inválido. Intente nuevamente.')
        continue

    if verificar_ganador(tablero, jugador_actual):
        tablero_1(tablero)
        print(f'¡Jugador "{jugador_actual}" ha ganado!')
        break

    if turno == 9:
        tablero_1(tablero)
        print('¡Empate!')
        break

    jugador_actual = 'O' if jugador_actual == 'X' else 'X'
    turno += 1
