#Ejercicio6. Escribir un programa que lea los datos de un archivo de texto, 
#que transforme cada línea en un diccionario y los añada a una lista. El archivo se llama agenda.txt.
#contacto = {id:,nombre:,apellido:,nac:}
#listaAgenda = [{},{},{},{}]from pprint import pprint
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
print(listaAgenda)
