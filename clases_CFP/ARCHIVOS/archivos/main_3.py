# Ejercicio 4: 
# Escribir un programa con una opción para leer las primeras n líneas de un archivo 
# y otra opción para leer las últimas n líneas de un archivo. Van a leer el archivo Soneto29.txt

dirSoneto = 'clases_CFP/ARCHIVOS/archivos/la_razon_que_te_demora.txt'
arcSoneto = open(dirSoneto)
contSoneto = arcSoneto.readlines()
arcSoneto.close()
print(contSoneto)