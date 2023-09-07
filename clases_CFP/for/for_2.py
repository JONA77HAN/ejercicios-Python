# Pedir 15 numeros y escribir la suma total.    USANDO FOR

suma_total = 0

for i in range(15):
    numero = int(input('ingrese un numero: '))
    suma_total += numero
print (suma_total)