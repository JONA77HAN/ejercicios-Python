# Ejercicio7. Pedir un número N, y mostrar todos los números del 1 al N.

i = 0
N = int(input('ingrese un numero: \n'))

for i in range (1,N+1):
    print (i)
    

# el + 1 lo utilizamos para que cuando usemos la funcion range, no nos quede afuera el numero N  