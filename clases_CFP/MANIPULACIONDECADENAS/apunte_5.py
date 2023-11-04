"""
    Justificación de texto con rjust(), ljust() y center():
Los métodos rjust() y ljust() devuelven una cadena con una cantidad de espacios agregados a la 
derecha o izquierda, respectivamente, para que contándolos junto a los caracteres de la 
cadena den el número que recibido en el argumento.
"""
print('Hola')
print('Hola'.rjust(25))
print('Hola'.rjust(50))
print('Hola'.rjust(75))
print('Hola'.rjust(100))
print('>'.rjust(125))
print('Hola'.rjust(100))
print('Hola'.rjust(75))
print('Hola'.rjust(50))
print('Hola'.rjust(25))
print('Hola')

print('Hola'.center(120))
print(' Hola '.center(120, '='))
