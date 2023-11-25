# Escribir un programa que pida al usuario dos números enteros 
# y muestre por pantalla la <n> entre <m> da un cociente <c> y 
# un resto <r> donde <n> y <m> son los números introducidos por el usuario, 
# y <c> y <r> son el cociente y el resto de la división entera respectivamente.
num_a = int(input('ingrese el primer numero entero: \n'))
num_b = int(input('ingrese el segundo numero entero: \n'))

cociente = round(num_a / num_b, 2)
resto = num_a % num_b

print(f'El resto de los numeros {num_a} y {num_b} es {resto} \ny el cociente de dichos numeros es {cociente}')
