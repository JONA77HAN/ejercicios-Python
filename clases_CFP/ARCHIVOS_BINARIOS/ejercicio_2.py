#Ejercicio2. Programar un archivo “Estudiantes.dat” con la estructura [[id, nombre,promedio]].
#Definir una función contarRegistros() que muestre cuantos alumnos ienen un promedio por arriba de 7.5 y cuáles son.
"""
import shelve
from random import randint

listInicio = []
nombre = ['Lidia','Ernesto','Maria','Florencio','Carolina','Juan','Pepe','Luis','Maxi','Gerardo']
for i in range(10):
	alumno = []
	alumno.append(i+1)
	alumno.append(nombre.pop(0))
	alumno.append(round(randint(50,100)/10,2))
	listInicio.append(alumno)
print(listInicio)
estuDir = './Estudiantes.dat'
estuBin = shelve.open(estuDir)
estuBin['listAlumnos'] = listInicio
estuBin.close()
"""
import shelve
from random import randint

def contarRegistros():
		arriba_de_75_count = 0
		print('ID'.ljust(5, '.') + 'Nombre'.center(15, '.') + 'Promedio'.rjust(10, '.'))

		for alumno in listado:
				if alumno[2] > 7.5:
						arriba_de_75_count += 1
						print(f'{alumno[0]}'.ljust(5, '.') + f'{alumno[1]}'.center(15, '.') + f'{alumno[2]}'.rjust(10, '.'))

		print(f'\nTotal de alumnos con promedio > 7.5: {arriba_de_75_count}')

listInicio = []
nombre = ['Lidia', 'Ernesto', 'Maria', 'Florencio', 'Carolina', 'Juan', 'Pepe', 'Luis', 'Maxi', 'Gerardo']

for i in range(10):
		alumno = []
		alumno.append(i + 1)
		alumno.append(nombre.pop(0))
		alumno.append(round(randint(50, 100) / 10, 2))
		listInicio.append(alumno)

estuDir = './Estudiantes.dat'
estuBin = shelve.open(estuDir)
estuBin['listAlumnos'] = listInicio
estuBin.close()

estuBin = shelve.open(estuDir)
listado = estuBin['listAlumnos'].copy()
estuBin.close()

print('ID'.ljust(5, '.') + 'Nombre'.center(15, '.') + 'Promedio'.rjust(10, '.'))
for alumno in listado:
		print(f'{alumno[0]}'.ljust(5, '.') + f'{alumno[1]}'.center(15, '.') + f'{alumno[2]}'.rjust(10, '.'))

contarRegistros()

