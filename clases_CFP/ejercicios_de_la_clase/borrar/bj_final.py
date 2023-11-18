from random import randint

puntaje_pc = 0 
puntaje_player = 0 
c = 0

while puntaje_pc < 17 or puntaje_player <= 21:
    carta_pc = randint(1,13)
    if carta_pc == 1 or carta_pc == 11 or carta_pc == 12 or carta_pc == 13:
        carta_pc = 10
    carta_player = randint(1,13)
    if carta_player == 1 or carta_player == 11 or carta_player == 12 or carta_player == 13:
        carta_player = 10
    c += 1     
    print ('"Blackjack" mano ' + str(c) + ':')
    print('-'*20)
    print( ' carta del croupier : ' + str(carta_pc))    
    puntaje_pc += carta_pc
    print( ' puntaje del croupier ---> ' + str(puntaje_pc))   
    print('-'*40) 
    print('          Tu carta: ' +  str(carta_player) )
    puntaje_player += carta_player
    print('          Tu puntaje ---> ' + str(puntaje_player))
    if puntaje_player < 22:
        respuesta = input('¿Queres otra carta? (s/n): ')
        print('-'*50)
        if respuesta == 's' or respuesta == 'si':
            continue
        else:
            print('tu puntaje final es ' + str(puntaje_player))
            break
    else:
        print('Estas fuera de juego ' + str(puntaje_player))
if puntaje_pc > 21:
    print ('Croupier fuera de juego ')
else:
    print ('Croupier plantado con ' + str(puntaje_pc))          

# Verificar quién gana
if puntaje_player > 21 and puntaje_pc > 21:
    print('Es un empate')
elif puntaje_player > 21:
    print('Croupier gana')
elif puntaje_pc > 21:
    print('¡¡ GANASTE !!')
elif puntaje_player == puntaje_pc:
    print('Es un empate')
elif puntaje_player > puntaje_pc:
    print('¡¡ GANASTE !!')
else:
    print('Croupier gana')
