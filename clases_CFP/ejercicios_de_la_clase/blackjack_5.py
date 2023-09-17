from random import randint

puntaje_pc = 0

while puntaje_pc < 17 :
    carta = randint(1,13)
    if carta == 1 or carta == 11 or carta == 12 or carta == 13:
        carta = 10
    print( 'carta del croupier : ' + str(carta))    
    puntaje_pc += carta
    print( ' Su puntaje ---> ' + str(puntaje_pc))
if puntaje_pc > 21:
    print ('Croupier fuera de juego ')
else:
    print ('Croupier plantado con ' + str(puntaje_pc))


        
    