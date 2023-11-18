# Ejercicio12.
# Pedir 10 números.
# Mostrar el promedio de los números positivos.
# Mostrar el promedio de los números negativos.
# Y la cantidad de ceros.

from random import randint

suma_positivos = 0
suma_negativos = 0
contador_positivos = 0
contador_negativos = 0
contador_cero = 0

for i in range(10):
    numero = randint(-5,5) #int(input('---> ingrese un numero <---\n'))
    print(f'el numero es {numero}')
    if numero > 0:
        suma_positivos += numero
        contador_positivos += 1
    elif numero < 0:
        suma_negativos += numero
        contador_negativos +=1
    else:
        contador_cero += 1

promedio_negativos = round (suma_negativos / contador_negativos, 2)
promedio_positivos = round (suma_positivos / contador_positivos, 2)

print(f'El promedio de los numeros positivos es {promedio_positivos}')
print(f'El promedio de los numeros negativos es {promedio_negativos}')
print(f'La cantidad de ceros es {contador_cero}')


#n=int(input('ingrese:\n))
#n=n%10
#print(n) 
