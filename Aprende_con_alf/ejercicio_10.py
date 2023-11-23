# Ejercicio 10
# Una juguetería tiene mucho éxito en dos de sus productos: 
# payasos y muñecas. Suele hacer venta por correo y la empresa 
# de logística les cobra por peso de cada paquete así que deben 
# calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. 
# Cada payaso pesa 112 g y cada muñeca 75 g. 
# Escribir un programa que lea el número de payasos y muñecas vendidos 
# en el último pedido y calcule el peso total del paquete que será enviado.

print(' Calculos de jugueteria '.center(50,'-'))
cantidad_payasos = int(input('Ingrese la cantidad de Payasos encargados: '))
cantidad_muñecas = int(input('Ingrese la cantidad de Muñecas encargadas: '))
peso_payasos = cantidad_payasos * 112
peso_muñecas = cantidad_muñecas * 75

peso_total_paquete = (peso_payasos + peso_muñecas) / 100

print(f'El peso total del paquete es de {peso_total_paquete} kg')