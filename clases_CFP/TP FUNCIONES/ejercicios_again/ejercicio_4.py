# https://peps.python.org/pep-0008/
# Ejercicio 4 
# Función a la que se le pasan dos enteros y muestra todos los números comprendidos entre ellos, inclusive.

#Ejemplo:
#Le paso 4 y 9
#Muestra 4 5 6 7 8 9
#Le paso 9 y 4

def numeros(o, p):
    for i in range(o, p + 1):
        print(i)
    if q > r:
         numeros (q, r)
    else:
         numeros (r, q )

r = int(input(' ingrese el numero -----> '))
q = int(input(' ingrese el numero -----> '))

numeros(r, q)





