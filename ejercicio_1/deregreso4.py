# Ejercicio 4: Números primos
# Escribe un programa que verifique si un número ingresado por el usuario es primo o no.

num = int(input('Ingresa un numero y te diré si es primo o no: '))

es_primo = True

if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            es_primo = False
            break

if es_primo:
    print(num, "es un número primo.")
else:
    print(num, "no es un número primo.")