from random import randint
#machine = croupier 
puntaje_pc = 0

while puntaje_pc < 17 :
    carta_pc = randint(1,13)
    if carta_pc == 1 or carta_pc == 11 or carta_pc == 12 or carta_pc == 13:
        carta_pc = 10
    print( 'carta del croupier : ' + str(carta_pc))    
    puntaje_pc += carta_pc
    print( ' Su puntaje ---> ' + str(puntaje_pc))
if puntaje_pc > 21:
    print ('Croupier fuera de juego ')
else:
    print ('Croupier plantado con ' + str(puntaje_pc))

