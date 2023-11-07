# Ejercicio5. Escribir un programa que pueda listar todas las carpetas y archivos del cwd por separado. 
# os.listdir, os.path.isfile/os.path.isdir.import os
listaArc = []
listaDir = []
for elemento in os.listdir():
	if os.path.isfile(elemento):
		listaArc.append(elemento)
	else:
		listaDir.append(elemento)

print('Archivos:')
for elemento in listaArc:
	print(elemento)
print('Carpetas:')
for elemento in listaDir:
	print(elemento)