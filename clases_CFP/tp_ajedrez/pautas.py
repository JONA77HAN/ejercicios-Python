from random import randint

# Definir los valores de las piezas
valores_piezas = {
    'Peon': 1,
    'Caballo': 3,
    'Alfil': 3,
    'Torre': 5,
    'Reina': 9,
    'Rey': 4
}

# Función para generar un tablero de ajedrez aleatorio
def generar_tablero_aleatorio():
    tablero = {
        'Blancas': {
            'Peones': randint(0, 8),
            'Caballos': randint(0, 2),
            'Alfiles': randint(0, 2),
            'Torres': randint(0, 2),
            'Reina': randint(0, 1),
            'Rey': 1
        },
        'Negras': {
            'Peones': randint(0, 8),
            'Caballos': randint(0, 2),
            'Alfiles': randint(0, 2),
            'Torres': randint(0, 2),
            'Reina': randint(0, 1),
            'Rey': 1
        }
    }
    return tablero

# Función para calcular el puntaje de un jugador en el tablero
def calcular_puntaje(tablero, equipo):
    puntaje = 0
    for pieza, valor in valores_piezas.items():
        puntaje += tablero[equipo][pieza] * valor
    return puntaje

# Función para verificar si el rey está en jaque
def esta_en_jaque(tablero):
    blancas = tablero['Blancas']
    negras = tablero['Negras']
    
    if (blancas['Rey'] == 1 and negras['Torres'] + negras['Reina'] >= 2) or \
       (negras['Rey'] == 1 and blancas['Torres'] + blancas['Reina'] >= 2):
        return True
    else:
        return False

# Generar un tablero aleatorio
tablero_aleatorio = generar_tablero_aleatorio()

# Calcular puntaje de cada jugador
puntaje_blancas = calcular_puntaje(tablero_aleatorio, 'Blancas')
puntaje_negras = calcular_puntaje(tablero_aleatorio, 'Negras')

# Verificar si un rey está en jaque
if esta_en_jaque(tablero_aleatorio):
    print("Rey en jaque.")
else:
    print("Rey seguro.")

# Imprimir el tablero y los puntajes
print("Tablero:")
print(tablero_aleatorio)
print("Puntaje Blancas:", puntaje_blancas)
print("Puntaje Negras:", puntaje_negras)
