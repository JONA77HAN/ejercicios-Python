# Ejercicio15. Pide un número (que debe estar entre 0 y 10) 
# Y mostrar la tabla de multiplicar de dicho número.
# Ejemplo:
# Se ingresa 4.
# Muestran:
# 4 x 0 = 0
# 4 x 1 = 4
#  ....
# 4 x 10 = 40

c = 0

numero = int(input('Ingrese un numero (del 1 al 10): '))

for i in range (10):
    c += 1
    multiplicacion = c * numero
    print (str(numero) + ' x ' + str(c) + ' = ' + str(multiplicacion))


    
 
