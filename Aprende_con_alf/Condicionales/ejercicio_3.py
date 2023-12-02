# Ejercicio 3
# Escribir un programa que pida al usuario dos números y muestre 
# por pantalla su división. Si el divisor es cero el programa debe mostrar un error.

divisor = int(input('Ingrese un divisor: '))
dividendo = int(input('Ingrese un dividendo: '))

if divisor <= 0:
    print('ERROR, ingrese un divisor positivo')
    divisor = int(input('Esta vez que sea un numero positivo: '))
    print('el resultado de la division es ' + str(dividendo / divisor))
else:
    print('el resultado de la division es ' + str(dividendo / divisor))
    