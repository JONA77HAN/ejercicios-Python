# Ejercicio7. Continuando el ejercicio 6.recorrer las personas de la lista 
# y para cada una mostrar todos sus valores de manera que sean fáciles de leer.from pprint import pprint
dirAgenda = './agenda.txt'
arcAgenda = open(dirAgenda)
contAgenda = arcAgenda.readlines()
arcAgenda.close()
listaAgenda = []
for linea in contAgenda:
	listaInfo = linea.split(';')
	contacto = {'id':'','nombre':'' ,'apellido':'','nac':''}
	for clave in contacto:
		contacto[clave]=listaInfo.pop(0)
	listaAgenda.append(contacto)

for contacto in listaAgenda:
	print(f'ID {contacto["id"]}'.center(30,'='))
	print('Nombre'.ljust(15,'.')+contacto["nombre"].rjust(15,'.'))
	print('Apellido'.ljust(15,'.')+contacto["apellido"].rjust(15,'.'))
	print('Nacimiento'.ljust(15,'.')+contacto["nac"].rjust(15,'.'))
