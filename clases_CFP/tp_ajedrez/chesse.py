import random
from random import randint
# Define las cantidades para cada pieza  --> blancas:
peon_blanco = randint(0, 8)
caballo_blanco = randint(0, 2)
alfil_blanco = randint(0, 2)
torre_blanca = randint(0, 2)
reina_blanca = randint(0, 1)
rey_blanco = 1
# Negras: 
peon_negro = int(randint(0, 8)) * '♟'
caballo_negro = randint(0, 2)
alfil_negro = randint(0, 2)
torre_negra = randint(0, 2)
reina_negra = randint(0, 1)
rey_negro = 1
# Transformando los numeros numeros en piezas

print(peon_negro)

piezas_en_tablero = []


print(piezas_en_tablero)