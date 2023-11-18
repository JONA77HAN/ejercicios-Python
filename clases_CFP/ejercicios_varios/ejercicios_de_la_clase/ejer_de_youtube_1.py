print(' --->  calculemos la raiz cuadrada de un numero   <--- ')

numero = int(input('ingrese un numero: \n'))

while numero < 0:
    print('error -> ingresaste un numero negativo')
    numero = int(input(
        'ingresa un numero positivo y calcularemos su raiz cuadrada: \n'))

raiz_cuadrada = numero ** 2

print(f'La raiz cuadrada de {numero} es {raiz_cuadrada}')
