from random import randint

puntaje_pc = 0

while puntaje_pc <= 17 :
    carta = randint(1,13)
    puntaje_pc += carta
    print(puntaje_pc)
    