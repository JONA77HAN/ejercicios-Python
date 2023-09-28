
# Ejercicio3.
# Leer 5 números, guardarlos en una lista 
# y a continuación realizar la media de los números positivos, 
# la media de los negativos 
# y contar el número de ceros.

#spam.insert(posicion,valor)

from random import randint

lista = [] 
c = 0
sum_positivos = 0
sum_negativos = 0
ceros = 0
c_positivos = 0
c_negativos = 0

for i in range(5):
    num = randint(-50,50)
    c += 1
    lista.insert(c, num)
    if num > 0:
        sum_positivos += num
        c_positivos += 1
    elif num < 0:
        sum_negativos += num
        c_negativos += 1
    elif num == 0:
        ceros += 1

if c_negativos == 0:
    promedio_negativos = 1
if c_positivos == 0:
    promedio_positivos = 1    

promedio_positivos = round(sum_positivos / c_positivos, 2)
promedio_negativos = round(sum_negativos / c_negativos, 2)

print(lista)
print('promedio de numeros positivos: ' + str(promedio_positivos))
print('promedio de numeros negativos: ' + str(promedio_negativos))
print('cantidad de ceros: ' + str(ceros))

# Ejercicio 4 
# Leer 10 números enteros, guardarlos en una lista. 
# Debemos mostrarlos en el siguiente orden: ... 
# el primero, el último, el segundo, el penúltimo, el tercero, el ante-penúltimo, etc.

from random import randint

lista = []

for i in range(10):
    num = randint(-50,50)
    lista.append(num)
print(lista)

print(lista[0])
print(lista[9])
print(lista[0])
print(lista[0])
print(lista[0])
print(lista[0])