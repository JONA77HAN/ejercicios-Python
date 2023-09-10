# Ejercicio4. 
# Pedir números hasta que se teclee uno negativo.
# mostrar cuántos números se han introducido.

numero = 1

if numero < 0:
    print ('se ingreso un numero negativo')
else:
    while numero > 0:
        numero = int(input('ingrese un nuevo numero: '))
        if numero < 0:
            print('fin del programa, se ingreso un numero negativo')
            break