# Ejercicio3. Leer números hasta que se introduzca un 0. 
# Para cada uno indicar si es par o impar. 


while True:
    numero = int(input('ingresa un numero: \n'))
    es_par = numero % 2
    if numero == 0:
        print('ingresaste "cero" fin del programa')
        break
    if es_par == 0:
        print ('es "par"')
    else:
        print('es "impar"') 
       

