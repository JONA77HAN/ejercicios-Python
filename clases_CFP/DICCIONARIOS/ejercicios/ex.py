verduras = {
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
    verdura = input('ingrese la verdura:\n')
    precio = verduras.get(verdura, False)
    if not precio:
        print('No hay esa verdura')
        continue
    cantidad = int(input('ingrese cuanto?:\n'))
    precio_total = precio * cantidad
    print(f'el precio total es {precio_total}')
    seguir = input('quieres calcular otro precio total (si o no):\n')
    if seguir.lower() == 'no':
        break