# Ejercicio3. Escribe un programa que pueda abrir un archivo y:
# a) Contar la cantidad de palabras.
# b) Encontrar la palabra más larga.
# c) Contar la frecuencia de cada palabra

from pprint import pprint
dirSoneto = './Soneto29.txt'
arcSoneto = open(dirSoneto)
contSoneto = arcSoneto.read()
arcSoneto.close()

listaPal = contSoneto.split()
cantPal = len(listaPal)
print(f'Cantidad de palabras {cantPal}')
masLarga = ''
dicPalabras = {}
for palabra in listaPal:
	if len(palabra.strip(',').strip('.')) > len(masLarga):
		masLarga = palabra.strip(',').strip('.')
	dicPalabras[palabra.strip(',').strip('.').lower()] = dicPalabras.get(palabra.strip(',').strip('.').lower(),0)+1
print(f'Palabra mas larga: {masLarga}')

pprint(dicPalabras)


