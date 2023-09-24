# Ejercicio 8 
# Definir una funcion que muestre en binario un número entre 0 y 255.

def binario(n):
    c = ''
    while n > 0:
        bit = n % 2
        c = str(bit) + c
        n //= 2
    print(c)

binario(9)        