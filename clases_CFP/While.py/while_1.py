#Ejercicio2. Leer un número e indicar si es positivo o negativo. El proceso se repetirá hasta que se introduzca un 0. 

#Resuelve: Carranza
num = ''
while num != 0:
    num = int(input('Ingrese un numero: '))
    if num > 0:
        print('numero positivo')
    else:
        print('numero negativo') 
print ('fin')        