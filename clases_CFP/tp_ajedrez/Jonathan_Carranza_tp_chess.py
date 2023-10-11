import random

def crear_tablero_aleatorio():
    tablero = [[" " for _ in range(8)] for _ in range(8)]
    piezas = ["P", "P", "P", "P", "P", "P", "P", "P", "C", "C", "A", "A", "T", "T", "R", "K"]
    random.shuffle(piezas)

    for fila in range(8):
        for col in range(8):
            pieza = piezas.pop()
            tablero[fila][col] = pieza

    return tablero

def calcular_puntaje(tablero):
    puntaje = {"P": 1, "C": 3, "A": 3, "T": 5, "R": 9, "K": 4}
    puntaje_blancas = sum(puntaje[pieza] for fila in tablero for pieza in fila if pieza.isupper())
    puntaje_negras = sum(puntaje[pieza] for fila in tablero for pieza in fila if pieza.islower())
    return puntaje_blancas, puntaje_negras

def esta_en_jaque(tablero):
    rey_pos = None

    for fila in range(8):
        for col in range(8):
            if tablero[fila][col] == "K":
                rey_pos = (fila, col)
                break

    if rey_pos is None:
        return False

    movimientos = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for mov in movimientos:
        fila, col = rey_pos[0] + mov[0], rey_pos[1] + mov[1]
        if 0 <= fila < 8 and 0 <= col < 8 and tablero[fila][col].islower():
            return True

    return False

def mostrar_tablero(tablero):
    for fila in tablero:
        print(" ".join(fila))
    print()

if __name__ == "__main__":
    tablero = crear_tablero_aleatorio()
    mostrar_tablero(tablero)
    puntaje_blancas, puntaje_negras = calcular_puntaje(tablero)
    print(f"Puntaje Blancas: {puntaje_blancas}")
    print(f"Puntaje Negras: {puntaje_negras}")
    if esta_en_jaque(tablero):
        print("Rey en jaque.")

