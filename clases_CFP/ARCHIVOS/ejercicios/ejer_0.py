# metodos write y read
# primero hago los cambios que quiero hacer
directorio = 'clases_CFP/ARCHIVOS/ejercicios/almohada.txt'
archivo = open(directorio, 'a')
contenido = archivo.write('\ntodas las hojas son del viento\nYa que las mueve hasta en la muerte')
archivo.close()

# ahora lo muestro
arc = open(directorio)
con = arc.read()
arc.close()
print(con)
