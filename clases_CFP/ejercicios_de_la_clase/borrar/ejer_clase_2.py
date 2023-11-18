# Ejercicio2. Leer un número e indicar si es positivo o negativo. 
# El proceso se repetirá hasta que se introduzca un 0. 



while True:
    numero = int(input('ingrese un numero: \n'))
    if numero < 0:
        print ('El numero ingresado es "negativo"')
    else:
        print ('El numero ingresado es "positivo"')
        if numero == 0:
            print ('fin del programa, ingresaste un "cero"')
            break

