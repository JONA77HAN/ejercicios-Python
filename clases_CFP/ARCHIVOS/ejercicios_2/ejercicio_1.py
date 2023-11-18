#Ejercicio1. Escribir un programa que pueda leer un archivo de texto completo.

import os

archivo = open('./hola.txt')
archivoContenido = archivo.read()
archivo.close()

print(archivoContenido)