# Ejercicio11. 
# Pedir un número y calcular su factorial. 
# Factorial de !5
# Si Ingresa 5
# 1*2*3*4*5
# Si Ingresa 7
# 1*2*3*4*5*6*7

n = int(input('ingrese un numero: '))
f = 1

for i in range(n):
    f = n * f
    print (f)  
