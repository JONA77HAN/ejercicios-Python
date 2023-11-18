def imprimir_tablero(tablero):
    for fila in tablero:
        print("|", end=" ")
        for casilla in fila:
            print(casilla, "|", end=" ")
        print("\n" + "-" * 9)

def verificar_ganador(tablero, jugador):
    for fila in tablero:
        if fila[0] == fila[1] == fila[2] == jugador:
            return True

    for columna in range(3):
        if tablero[0][columna] == tablero[1][columna] == tablero[2][columna] == jugador:
            return True

    if tablero[0][0] == tablero[1][1] == tablero[2][2] == jugador:
        return True
    if tablero[0][2] == tablero[1][1] == tablero[2][0] == jugador:
        return True

    return False

def jugar_tateti():
    tablero = [[" " for _ in range(3)] for _ in range(3)]
    jugador_actual = "X"
    jugadas = 0

    while True:
        imprimir_tablero(tablero)
        fila = int(input(f"Jugador '{jugador_actual}', elige una fila (0, 1, 2): "))
        columna = int(input(f"Jugador '{jugador_actual}', elige una columna (0, 1, 2): "))

        if tablero[fila][columna] == " ":
            tablero[fila][columna] = jugador_actual
            jugadas += 1
        else:
            print("Casilla ocupada. Elige otra.")
            continue

        if verificar_ganador(tablero, jugador_actual):
            imprimir_tablero(tablero)
            print(f"¡Jugador '{jugador_actual}' ha ganado!")
            break

        if jugadas == 9:
            imprimir_tablero(tablero)
            print("¡Empate!")
            break

        jugador_actual = "O" if jugador_actual == "X" else "X"

if __name__ == "__main__":
    jugar_tateti()
