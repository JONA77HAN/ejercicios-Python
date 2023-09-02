# Ejercicio 14
# Pedir una hora de la forma hora, minutos y segundos.  
# y mostrar la hora en el segundo siguiente.

print('ingrese la hora: ')
hora = int(input()) 

print('ingrese los minutos: ')
minuto = int(input())

print('ingrese los segundos: ')
segundo = int(input())

segundo += 1

if segundo > 59:
    segundo = 00
    minuto += 1

if minuto > 59:
    minuto = 00
    hora += 1
    
if hora > 24:
    hora = 1
    minuto = 00
    segundo = 00

print('La hora en el siguiente segundo sera ' + str(hora) + ':' + str(minuto) + ':' + str(segundo) + ' hs' )            
