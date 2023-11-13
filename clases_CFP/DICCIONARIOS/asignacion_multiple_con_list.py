# La función list(spam.keys) toma los valores de la dict_key y los devuelve en forma de lista. 
# Podemos utilizar el truco de asignación múltiple en un ciclo for para asignar la clave y el valor a 
# distintas variables. 
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
for i in lista_verduras.keys():
    print(i)
print('remolacha' not in lista_verduras)
verdura = input('elije una verdura: \n')
print(lista_verduras.get(verdura, 'no hay peras'))