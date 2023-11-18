# Objetivo del juego: Ganarle al Croupier (la computadora)

# Para generar cartas, generar al azar un número entre 1 y 13.

# El 1, 11, 12 y 13, valen 10.

# Cuando empieza la ronda generar 1 carta para cada jugador.

# El croupier debe pedir otra carta si suma 16 o menos.
# El croupier debe plantarse si suma 17 o más.

# El jugador puede pedir otra carta o plantarse.
# Gana el jugador que se acerque más al 21 sin pasarse.

# Pierde el jugador que se pase de 21. Si ambos se pasan o llegan al mismo número, hay empate.

#Empieza
#Croupier roba 4 -> pedir
#Jugador roba 10 -> plantarse o pedir

from random import randint

suma_croupier = 0
suma_jugador = 0
roba_croupier_1 = randint(1,13)
roba_jugador_1 = randint(1,13)

if roba_croupier_1 == 1 or roba_croupier_1 == 11 or roba_croupier_1 == 12 or roba_croupier_1 == 13:
    roba_croupier_1 = 10

print('Blackjack')
print('primer mano -->') 
print (f'   Carta croupier: {roba_croupier_1}')

roba_croupier_2 = randint(1,13)
if roba_croupier_2 == 1 or roba_croupier_2 == 11 or roba_croupier_2 == 12 or roba_croupier_2 == 13:
    roba_croupier_2 = 10
    suma_croupier = roba_croupier_1 + roba_croupier_2

print('segunda mano -->') 
print(f'   Carta croupier: {roba_croupier_2} --> en total suma {suma_croupier} ')

if suma_croupier >= 17:
    print(f'se planta con {suma_croupier}')
else:
    roba_croupier_3 = randint(1,13)
    if roba_croupier_3 == 1 or roba_croupier_3 == 11 or roba_croupier_3 == 12 or roba_croupier_3 == 13:
        roba_croupier_3 = 10
        suma_croupier += roba_croupier_3
        print('segunda mano -->') 
        print(f'   Carta croupier: {roba_croupier_3} --> en total suma {suma_croupier} ')
        if suma_croupier >= 17:
            print(f'se planta con {suma_croupier}')
        else:
            print('no se')
            

#cartas del jugador:
if roba_jugador_1 == 1 or roba_jugador_1 == 11 or roba_jugador_1 == 12 or roba_jugador_1 == 13:
    roba_jugador_1 = 10

print (f'   Tu carta: {roba_jugador_1}')
respuesta_1 = str(input(f'¿Querés otra? (si/no): '))
if respuesta_1 == 'si' or respuesta_1 == 's':
    roba_jugador_2 = randint(1,13)
    suma_jugador = roba_jugador_1 + roba_jugador_2
    print(f'   Tu carta : {roba_jugador_2} --> en total sumás {suma_jugador} ')
    respuesta_2 = str(input(f'¿Querés otra carta? (si/no): '))






        

    
