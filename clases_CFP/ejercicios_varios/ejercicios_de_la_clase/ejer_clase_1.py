# Ejercicio1. Pedir un número y mostrar su cuadrado, 
# Repetir el proceso hasta que se introduzca un número negativo.
cuadrado_del_numero = 1

while True:
    numero = int(input('ingresa un numero: \n'))
    cuadrado_del_numero = numero **2
    print(cuadrado_del_numero)
    if numero < 0:
        break