# Ejercicio5. Pedir números hasta que se teclee un 0. 
# Mostrar la suma de todos los números introducidos.

suma = 0

while True:
    numero = int(input('ingrese un numero: \n'))
    suma += numero
    if numero == 0:
        print (f'La suma de todos los numeros ingresados es {suma}')
        break
