# Depuracion.
# EjercicioRecursivo. Diseñar una funcion recursiva que calcule el factorial de un numero.

# Ingreso 7:
# 1x2x3x4x5x6x7
# 7x6x5x4x3x2x1
# La funcion me devuelve 
# 5040

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(7))