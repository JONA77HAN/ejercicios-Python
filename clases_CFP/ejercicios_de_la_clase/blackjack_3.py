from random import randint

puntaje_pc = 0
puntaje_player = 0

#primer mano
mano_pc = randint(1,13)
if mano_pc == 1 or mano_pc == 11 or mano_pc == 12 or mano_pc == 13:
    mano_pc = 10
print('primer mano -->') 
print (f'   Carta croupier: {mano_pc}')

mano_player = randint(1,13)
if mano_player == 1 or mano_player == 11 or mano_player == 12 or mano_player == 13:
    mano_player = 10
print (f'   Tu carta : {mano_player}')

#segunda mano
mano_pc_2 = randint(1,13)
if mano_pc_2 == 1 or mano_pc_2 == 11 or mano_pc_2 == 12 or mano_pc_2 == 13:
    mano_pc_2 = 10
puntaje_pc = mano_pc + mano_pc_2    
print('segunda mano -->') 
print(f'   Carta croupier: {mano_pc_2} --> en total suma {puntaje_pc} ')
if puntaje_pc >= 17:
    print (f'Croupier se planta con {puntaje_pc} puntos')
else:
    mano_pc_3 = randint()


