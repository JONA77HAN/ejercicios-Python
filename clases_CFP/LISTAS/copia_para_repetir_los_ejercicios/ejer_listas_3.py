# Ejercicio 3:
# Leer 5 números 
# guardarlos en una lista y a continuación 
# realizar la media de los números positivos, 
# la media de los negativos y 
# contar el "número" de ceros.

# spam.insert(posicion,valor)

from random import randint

lista = []
c_positivos = 0 
s_positivos = 0
c_negativos = 0
s_negativos = 0
ceros = 0

for i in range(5):
    num = randint(-100,100)
    lista.insert(i, num)
    if num < 0:
        c_negativos += 1
        s_negativos += num
    elif num > 0:
        c_positivos += 1
        s_positivos += num
    else:
        ceros += 1
print(lista)   

if c_positivos == 0:
    print('no hubo numeros positivos')
else:
    promedio_positivos = round (s_positivos / c_positivos, 2)
    print(f'el promedio de los numeros positivos ingresados es {promedio_positivos}')
if c_negativos == 0:
    print('no hubo numeros negativos')
else:
    promedio_negativos = round (s_negativos / c_negativos, 2) 
    print(f'el promedio de los numeros negativos ingresados es {promedio_negativos}')  

if ceros == 0:
    print('no hubo ceros') 
else:
    print(f'el numero de ceros fue de {ceros}')   






           






