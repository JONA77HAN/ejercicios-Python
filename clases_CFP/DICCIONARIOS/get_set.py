        # El método get() 
# Para no tener que prevenir los errores de no encontrar una clave dentro de un diccionario existe 
# el método get(). Este método toma 2 argumentos: la clave del valor que estamos buscando, y el 
# valor que devolverá en caso de no encontrarlo.  
lista_verduras = {
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
        respuesta = input('elije una fruta: \n')
        if respuesta in lista_verduras:
                print(lista_verduras.get(respuesta, f'no hay {respuesta}'))
                
                

