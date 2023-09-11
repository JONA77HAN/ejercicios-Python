# Ejercicio6. Pedir números hasta que se introduzca uno negativo, 
# Y calcular el promedio.

suma = 0
contador = 0
promedio = 0

while True:
    numero = int(input('ingrese un numero: '))
    contador += 1
    suma += numero
    if numero < 0:
        promedio = suma / contador
        print (f'se ingresaron {contador} numeros. \nEl promedio de los mismos es {promedio}')
        break

