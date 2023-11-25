# Escribir un programa que pregunte al usuario una cantidad a invertir, 
# el interés anual y el número de años, y muestre por pantalla 
# el capital obtenido en la inversión.
saludo_inicial = ' Programa '.center(20, '-')
print(saludo_inicial)

cantidad_a_invertir = int(input('Que cantidad de dinero desea invertir: \n'))
cuantos_años = int(input('Cuantos años deseas invertir? : \n'))
interes_anual = cantidad_a_invertir * 20 / 100 + cantidad_a_invertir
capital_obtenido = interes_anual * cuantos_años

print(f'el interes anual ganado es de {interes_anual}')
print(f'Tu capital obtenido en {cuantos_años} años, es de {capital_obtenido}')
