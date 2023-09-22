#Ejercicio7. Diseña una función que decida si un número es primo.
#Aclaraciones:
#Es primo si tiene solo 2 divisores (1 y si mismo)
#Un numero es divisor de otro si el modulo/resto les da 0.

#Ejemplo:
#Le paso 5
#Devuelve "Es primo"/True
#Le paso 8
#Devuelve "No es primo"/False

#Continuamos a las 18:35

def es_primo(numero):
    if numero <= 1:
        return False  # Los números menores o iguales a 1 no son primos
    
    # Comprobar si el número es divisible por algún número desde 2 hasta la raíz cuadrada de numero
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False  # El número es divisible, por lo tanto no es primo
    
    return True  # Si no es divisible por ningún número, es primo

# Ejemplo de uso:
numero = 43  # Puedes cambiar el número que deseas verificar
if es_primo(numero):
    print(f"{numero} es primo")
else:
    print(f"{numero} no es primo")
