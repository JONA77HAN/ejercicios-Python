#Ejercicio8. Pedir una nota de 1 a 10 y mostrarla de la forma: Insuficiente(1-3), 
#Regular(4-5), Bien(6-7), Muy Bien(8-9), Sobresaliente(10)

print('ingrese su nota: ')
nota = int(input())

if nota <= 3:
    print('Insuficiente')
if nota == 4 or nota == 5:   
    print('Regular')
if nota == 6 or nota == 7:
    print('Bien')
if nota == 8 or nota == 9:    
    print('Muy bien')
if nota == 10:    
    print('Sobresaliente')