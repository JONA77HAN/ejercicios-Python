#Trabajo Integrador.

#Programar un juego de Ta-Te-TI / La vieja:
#El tablero son 9 casilleros en un 3x3.
#Jugador1 y Jugador2 se toman turnos para poner una X o un O, respectivamente.
#Checkear luego de cada turno si hay un ganador.

# Función para imprimir el tablero
def imprimir_tablero(tablero):
    for fila in tablero:
        print(" | ".join(fila))
        print("-" * 9)

# Función para verificar si hay un ganador
def verificar_ganador(tablero, jugador):
    # Verificar filas
    for fila in tablero:
        if all([casilla == jugador for casilla in fila]):
            return True

    # Verificar columnas
    for col in range(3):
        if all([fila[col] == jugador for fila in tablero]):
            return True

    # Verificar diagonales
    if all([tablero[i][i] == jugador for i in range(3)]) or all([tablero[i][2 - i] == jugador for i in range(3)]):
        return True

    return False

# Función principal del juego
def jugar_tateti():
    tablero = [[" " for _ in range(3)] for _ in range(3)]
    jugador = "X"
    jugadas = 0

    while True:
        imprimir_tablero(tablero)
        fila = int(input(f"Jugador {jugador}, elige una fila (0, 1, 2): "))
        columna = int(input(f"Jugador {jugador}, elige una columna (0, 1, 2): "))

        if fila < 0 or fila > 2 or columna < 0 or columna > 2 or tablero[fila][columna] != " ":
            print("Movimiento inválido. Intenta de nuevo.")
            continue

        tablero[fila][columna] = jugador
        jugadas += 1

        if verificar_ganador(tablero, jugador):
            imprimir_tablero(tablero)
            print(f"¡Jugador {jugador} ha ganado!")
            break
        elif jugadas == 9:
            imprimir_tablero(tablero)
            print("¡Empate!")
            break

        jugador = "O" if jugador == "X" else "X"

if __name__ == "__main__":
    jugar_tateti()

