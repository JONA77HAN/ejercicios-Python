# metodos write y read
# primero hago los cambios que quiero hacer
directorio = 'clases_CFP/ARCHIVOS/ejercicios/almohada.txt'
archivo = open(directorio, 'a')
contenido = archivo.write('')
archivo.close()

# ahora lo muestro
arc = open(directorio)
con = arc.read()
arc.close()
print(con)
