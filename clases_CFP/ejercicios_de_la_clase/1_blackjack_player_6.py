from random import randint
# player 
puntaje_player = 0 

while puntaje_player <= 21 :
    carta_player = randint(1,13)
    if carta_player == 1 or carta_player == 11 or carta_player == 12 or carta_player == 13:
        carta_player = 10
    puntaje_player += carta_player
    print('Tu carta: ' +  str(carta_player) )
    print('Tu puntaje: ' + str(puntaje_player))
    if puntaje_player < 22:
        respuesta = input('¿Queres otra carta? (s/n): ')
        if respuesta == 's' or respuesta == 'si':
            continue
        else:
            print('tu puntaje final es ' + str(puntaje_player))
            break
    else:
        print('Estas fuera de juego ' + str(puntaje_player))    