#DICCIONARIOS
#Ejercicio4.  Crear un programa que nos permita guardar los nombres de los alumnos de una clase y las notas que han obtenido.
#Cada alumno puede tener distinta cantidad de notas.
#Guardar la información en un diccionario cuyas claves serán los nombres de los alumnos y los valores serán listas con las notas de cada alumno.
#El programa pedirá el número de alumnos que vamos a introducir, pedirá su nombre e irá pidiendo sus notas hasta que introduzcamos un cero.
#Al final el programa nos mostrará la lista de alumnos y la nota media obtenida por cada uno de ellos.
#Nota: si se introduce el nombre de un alumno que ya existe el programa nos dará un error y nos volvera a pedir un nombre.

alumnos = {}
num_alumnos = int(input("Ingrese el número de alumnos: "))
for i in range(num_alumnos):
		nombre = input('Ingrese el nombre del alumno ')
		while nombre in alumnos:
				print("¡Error! Este alumno ya está registrado. Introduzca un nombre diferente.")
				nombre = input('Ingrese el nombre del alumno ')
		notas = []
		nota = int(input('Ingrese una nota para alumno o (0 para finalizar): '))
		while nota != 0:
				notas.append(nota)
				nota = int(input('Ingrese una nota para alumno o (0 para finalizar): '))

		alumnos[nombre] = notas.copy()
for nombre, notas in alumnos.items():
		nota_media = round(sum(notas) / len(notas),2)
		print(nombre, 'la nota media es ', nota_media)