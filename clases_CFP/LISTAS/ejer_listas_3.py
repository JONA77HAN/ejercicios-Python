# Ejercicio 3:
# Leer 5 números 
# guardarlos en una lista y a continuación 
# realizar la media de los números positivos, 
# la media de los negativos y 
# contar el "número" de ceros.

# spam.insert(posicion,valor)

from random import randint

lista = []
c = 0
c_posit = 0
c_negat = 0
ceros = 0
suma_positivos = 0
suma_negativos = 0

# leemos cinco numeros de forma aleatoria
for i in range(5):
    num = randint(-50,50)
    c += 1
    lista.insert(c, num)
    if num > 0:
        c_posit += 1 
        suma_positivos += num 
    elif num < 0:
        c_negat += 1
        suma_negativos += num 
    else:
        ceros += 1

# sacamos los promedios de numeros negativos y positivos



             
print (lista)    