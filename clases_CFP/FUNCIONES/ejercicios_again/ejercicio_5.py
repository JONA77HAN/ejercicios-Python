#Ejercicio5. Realizar una función que calcule (muestre en pantalla) el área o el volumen de un cilindro, según se especifique. Para distinguir un caso de otro se le pasará el carácter 'a' (para área) o 'v' (para el volumen). Además, hemos de pasarle a la función el radio y la altura.
#Volumen = Pi*Radio^2*altura
#Area = 2*Pi*Radio*Altura

#Resuelve: Carranza

def calcular_cilindro(tipo, radio, altura):
    if tipo == 'a':
        area = round(2 * 3.141592 * radio * altura, 2)
        print('El área del cilindro es: ' + str(area))
    elif tipo == 'v':
        volumen = round(3.141592 * radio**2 * altura, 2)
        print('El volumen del cilindro es: ' + str(volumen))
    else:
        print('Tipo no válido. Ingrese "a" para área o "v" para volumen'  )

tipo = input('ingrese el tipo "a" para área o "v" para volumen: ')
radio = int(input('ingrese el radio: '))
altura = int(input('ingrese la altura: '))

calcular_cilindro(tipo, radio, altura)  