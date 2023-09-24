#Ejercicio3. Ídem una versión que calcule el máximo de 3 números.

def maximo(m, n, o):
    if m > n and m > o:
        print(f'el mas grande es {m}')
    elif n > o and n > m:
        print(f'el mas grande es {n}')
    else:
        print(f'el mas grande es {o}')

maximo(11,1011,54)