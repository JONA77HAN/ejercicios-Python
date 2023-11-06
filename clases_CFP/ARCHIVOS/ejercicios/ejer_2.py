# Ejercicio2. Escribir un programa que pueda agregar texto a un archivo y luego mostrarlo.

rima_direccion = 'C:/Users/54112/Desktop/aprendiendo_PYTHON/clases_CFP/ARCHIVOS/ejercicios/rima.txt'
rima_archivo =  open(rima_direccion, 'a')
texto = input('ingrese texto: ')
rima_archivo.write(texto)
rima_archivo.close()
rima_archivo = open(rima_direccion)
rima_contenido = rima_archivo.read()
rima_archivo.close()
print(rima_contenido)
