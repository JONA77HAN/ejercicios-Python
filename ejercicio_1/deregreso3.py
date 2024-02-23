# Escribe un programa que convierta una temperatura en grados Celsius a grados Fahrenheit. 
# La fórmula de conversión es: Fahrenheit = (Celsius × 9/5) + 32.

temperaturaEnGrados = int(input('ingresa la temperatura: '))
fahrenheit = (temperaturaEnGrados*9/5) + 32
print(f'La temperatura en fahrenheit es {fahrenheit} grados')