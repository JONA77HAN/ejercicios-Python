# Programar un juego de Ta-Te-TI:
# El tablero son 9 casilleros
# Jugador1 y Jugador2 se toman turnos para poner una X o un O, respectivamente.
# Checkear luego de cada turno si hay un ganador.

# Generando tablero y bienvenida al juego.
def tablero_1(tablero):
    print('TA TE TI')
    print(tablero[0] + '  /  ' + tablero[1] + '  /  ' + tablero[2])
    print('-'*15)
    print(tablero[3] + '  /  ' + tablero[4] + '  /  ' + tablero[5])
    print('-'*15)
    print(tablero[6] + '  /  ' + tablero[7] + '  /  ' + tablero[8])

# Inicializa el tablero como una lista de strings vacíos
tablero = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
tablero_1(tablero)
eleccion_x = int(input('Jugador "X"\nIngrese su posicion: '))


