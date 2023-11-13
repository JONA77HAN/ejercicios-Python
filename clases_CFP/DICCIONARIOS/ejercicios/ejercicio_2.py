
# Ejercicio 2: Escribir un programa que contenga en un diccionario los precios 
# de una verdulería. El programa pedirá el nombre de la verdura y 
# la cantidad que se ha vendido y nos mostrará el precio final de la venta 
# a partir de los datos guardados en el diccionario. 
# Si la verdura no existe nos dará un error. Tras cada consulta el programa 
# nos preguntará si queremos hacer otra consulta.
"""
verduras = {'tomate':20,'cebolla':15,'zanahoria':30, 'papa':20}
while True:
	verdura = input('que verdura queres comprar ')
	precio = verduras.get(verdura,False)
	if not precio:
		print('ERROR: No hay esa verdura')
		continue
	cantidad = int(input('cuanto se vendio '))
	precio_total = precio * cantidad
	print('el precio total es $' + str(precio_total))
	seguir = input('quieres hacer otra consulta ')
	if seguir == 'no':
		break
"""

verduras_2 = {
	'batata': 35,
	'brocoli': 120,
	'albahaca': 25,
	'puerro': 30,
	'naranja': 45,
	'mandarina': 20,
	'banana': 46,
	'manzana': 80,
	'rucula': 100
}
while True:
	verdu = input('ingrese la verdura, para saber el precio: \n')
	precio_2 = verduras_2.get(verdu, False)	
	if not precio_2:
		print('No hay esa verdura')
		continue
	cantidad_2 = int(input('que cantidad: \n'))
	precio_total_2 = precio_2 * cantidad_2
	print(f'el precio total es {precio_total_2}')
	seguir_2 = input('quieres calcular otro precio total (si o no):\n')
	if seguir_2.lower() == 'no':
		break
