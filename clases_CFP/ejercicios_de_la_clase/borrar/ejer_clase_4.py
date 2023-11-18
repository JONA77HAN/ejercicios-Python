# Ejercicio4. Pedir números hasta que se teclee uno negativo, 
# Y mostrar cuántos números se han introducido.

contador = 0

while True:
    numero = int(input('ingrese un numero: \n'))
    contador+= 1
    if numero < 0:
        print('se ingreso un número negativo. Fin del programa.')
        print(f'ingresaste {contador} numeros')
        break