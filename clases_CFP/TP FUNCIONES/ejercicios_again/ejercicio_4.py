# Ejercicio 4 
# Función a la que se le pasan dos enteros y muestra todos los números comprendidos entre ellos, inclusive.
# Ejemplo:
# Le paso 4 y 9
# Muestra 4 5 6 7 8 9
# Le paso 9 y 4

def entre_ellos(M,N):
    for i in range(M,N+1):
        print(i) 
    for f in range(N,M+1):
        print(f)   
   
M = int(input('ingrese el valor de M: '))
N = int(input('ingrese el valor de N: '))     

if M > N:
	entre_ellos(M,N)
else:
	entre_ellos(N,M)



