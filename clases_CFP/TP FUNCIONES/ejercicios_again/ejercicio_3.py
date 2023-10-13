#Ejercicio3. Ídem una versión que calcule el máximo de 3 números.

def maximos (m, n, ñ):
    if m > n and m > ñ:
        print('el maximo es el primero')
    elif n > m and n > ñ:
        print('el segundo ingresado es el maximo')
    else:
        print('el maximo es el ultimo')
maximos(10103, 5500, 600)            