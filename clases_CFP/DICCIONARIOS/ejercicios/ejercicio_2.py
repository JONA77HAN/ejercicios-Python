
#Ejercicio2. Escribir un programa que contenga en un diccionario los precios de una verdulería. El programa pedirá el nombre de la verdura y la cantidad que se ha vendido y nos mostrará el precio final de la venta a partir de los datos guardados en el diccionario. Si la verdura no existe nos dará un error. Tras cada consulta el programa nos preguntará si queremos hacer otra consulta.

#Resuelve: Cayoja

verduras = {'tomate':20,'cebolla':15,'zanahoria':30, 'papa':20}

while True:
	verdura = input('que verdura queres comprar ')
	"""
	try:
		precio = verduras[verdura]
	except:
		print('ERROR: NO HAY ESA VERDURA')
		continue

	if verdura in verduras:
		precio = verduras[verdura]
	else:
		print('ERROR: NO HAY ESA VERDURA')
		continue
	"""
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
