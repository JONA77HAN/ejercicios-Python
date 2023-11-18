from random import randint

# Inicialización de puntajes
puntaje_pc = 0
puntaje_player = 0

while True:
    # Primer mano
    carta_player = randint(1, 13)
    if carta_player == 1 or carta_player == 11 or carta_player == 12 or carta_player == 13:
        carta_player = 10
    puntaje_player += carta_player
    print('Tu carta: ' + str(carta_player))
    
    carta_pc = randint(1, 13)
    if carta_pc == 1 or carta_pc == 11 or carta_pc == 12 or carta_pc == 13:
        carta_pc = 10
    puntaje_pc += carta_pc
    print('Carta del croupier: ' + str(carta_pc))

    # Turnos adicionales
    while puntaje_player <= 21:
        respuesta = input('¿Quieres otra carta? (s/n): ')
        if respuesta.lower() == 's' or respuesta.lower() == 'si':
            carta_player = randint(1, 13)
            if carta_player == 1 or carta_player == 11 or carta_player == 12 or carta_player == 13:
                carta_player = 10
            puntaje_player += carta_player
            print('Tu carta: ' + str(carta_player))
        else:
            break

    while puntaje_pc < 17:
        carta_pc = randint(1, 13)
        if carta_pc == 1 or carta_pc == 11 or carta_pc == 12 or carta_pc == 13:
            carta_pc = 10
        puntaje_pc += carta_pc
        print('Carta del croupier: ' + str(carta_pc))

    # Determinar el resultado
    print('Tu puntaje: ' + str(puntaje_player))
    print('Puntaje del croupier: ' + str(puntaje_pc))
    if puntaje_pc > 21 or (puntaje_player <= 21 and puntaje_player > puntaje_pc):
        print('¡Ganaste!')
    elif puntaje_player == puntaje_pc:
        print('Es un empate.')
    else:
        print('La máquina (croupier) gana.')

    # Preguntar si desea jugar de nuevo
    jugar_de_nuevo = input('¿Quieres jugar de nuevo? (s/n): ')
    if jugar_de_nuevo.lower() != 's':
        break
