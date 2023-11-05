#Ejercicio1. Escribir un programa que pueda leer un archivo de texto completo.
import os
archivo = open('C:/Users/54112/Desktop/aprendiendo_PYTHON/clases_CFP/ARCHIVOS/ejercicios/rima.txt')
archivo_contenido = archivo.read()
archivo.close()

print(archivo_contenido)