# Ejercicio3. Escribe un programa que pueda abrir un archivo y:
# a) Contar la cantidad de palabras.
# b) Encontrar la palabra más larga.
# c) Contar la frecuencia de cada palabra
from pprint import pprint
archivo = open('clases_CFP/ARCHIVOS/archivos/hablando_de_la_libertad.txt')
contenido = archivo.read()
archivo.close()

lista_palabras = contenido.split()
cantidad_palabras = len(lista_palabras)
print(f'La cantidad de palbras es {cantidad_palabras}')

palabra_mas_larga = ''
dic_palabras = {}

for palabra in lista_palabras:
    palabra_sin_puntuacion = palabra.strip(',').strip('.')
    if len(palabra_sin_puntuacion) > len(palabra_mas_larga):
        palabra_mas_larga = palabra_sin_puntuacion
        dic_palabras[palabra_sin_puntuacion.lower()] = dic_palabras.get(palabra_sin_puntuacion.lower(), 0)+1

print(f'La palabra mas larga es {palabra_mas_larga}')

pprint(dic_palabras)