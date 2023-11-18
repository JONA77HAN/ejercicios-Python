#Ejercicio2. Diseñar una función que tenga como parámetros dos números, y que calcule el máximo.
def max(N,M):
  if N > M:
    print('El '+str(N)+' es mas grande')
  else:
    print('El '+str(M)+' es mas grande')
         
N = int(input('Ingrese un numero:  '))
M = int(input('Ingrese un numero:  '))

max(N,M)
