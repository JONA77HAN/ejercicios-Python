# Ejercicio5. 
# Realizar una función que calcule: 
# (muestre en pantalla) el área o el volumen de un cilindro, según se especifique. 
# Para distinguir un caso de otro se le pasará el carácter 'a' (para área) o 'v' (para el volumen). 
# Además, hemos de pasarle a la función el radio y la altura.
# Volumen = Pi*Radio^2*altura
# Area = 2*Pi*Radio*Altura

def calcular(tipo, radio, altura):
    if tipo == 'a':
        area = round(2*3.14*altura, 2)
        print(f'el area es de {area}')
    elif tipo == 'v':
        volumen = round(3.14*radio**2*altura, 2)
        print(f'el volumen es de {volumen}')
    else:
        print ('ingrese un tipo valido, "a" o "v"')    

a = input('ingrese el tipo: ')
b = int(input('ingrese el radio: '))
c = int(input('ingrese la altura: '))

calcular(a, b, c)

