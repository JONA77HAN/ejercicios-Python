#Ejercicio3.Leer números hasta que se introduzca un 0. Para cada uno indicar si es par o impar. 

#Un numero es par si su modulo o resto 2 es 0.

#Resuelve: Herrera

num = ''
while not num == 0:
    num = int(input('Ingrese un numero: '))
    if num % 2 == 0:
        print('numero es par')
    else:
        print('numero es impar') 
print ('fin del ejercicio')    