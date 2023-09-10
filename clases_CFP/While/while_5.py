# Ejercicio4. 
# Pedir números hasta que se teclee uno negativo.
# mostrar cuántos números se han introducido.

num = 0
contador = 0

while True :
    num = int(input('Ingrese un numero: '))
    contador += 1
    if num < 0:
        print ('numero negativo')
        break
print('ingresaste ' + str(contador) + ' veces')