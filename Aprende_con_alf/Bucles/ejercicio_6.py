# Ejercicio 6
# Escribir un programa que pida al usuario un número entero y 
# muestre por pantalla un triángulo rectángulo como el de más abajo, 
# de altura el número introducido.

# Solicitar al usuario que introduzca un número entero positivo.
n = int(input("Introduce la altura del triángulo (entero positivo): "))

# Utilizar un bucle for para iterar desde 0 hasta n-1 (inclusive).
for i in range(n):
    # En cada iteración del bucle externo, utilizar otro bucle for para imprimir "*" en la misma línea.
    # El bucle interno va desde 0 hasta i, de modo que en la primera iteración imprimirá 1 "*", 
    # en la segunda iteración imprimirá 2 "*", y así sucesivamente.
    for j in range(i+1):
        print("*", end="")
    
    # Después de imprimir los "*" en una línea, pasar a la siguiente línea.
    print("")
