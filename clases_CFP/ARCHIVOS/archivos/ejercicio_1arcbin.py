#Ejercicio1.Programar un archivo binario llamado “Libros.dat” con esta estructura [[libroNumero,libroNombre, autor, precio]].
#a) Definir una función para que un usuario pueda agregar libros al archivo binario.
#b) Defnir una función que acepte el nombre de un autor y devuelva cuantos libros del mismo hay en el archivo binario.
import shelve

def mostrar_biblioteca():
	biblioShelf = shelve.open('Libros.dat')
	libros = biblioShelf['biblioteca'].copy()
	for libro in libros:
		print(libro)
	biblioShelf.close()
def agregar_libro_arch_bin():
	biblioShelf = shelve.open('Libros.dat')
	libros = biblioShelf['biblioteca'].copy()
	libro = []
	libro.append(input('Numero del libro: '))
	libro.append(input('Nombre del libro: '))
	libro.append(input('Autor del libro: '))
	libro.append(input('Precio del libro: '))
	libros.append(libro)
	biblioShelf['biblioteca'] = libros.copy()
	biblioShelf.close()
def cantidad_libros_autor():
	autor = input('ingrese el nombre del autor: ').lower()
	biblioShelf = shelve.open('Libros.dat')
	libros = biblioShelf['biblioteca'].copy()
	biblioShelf.close()
	cant_libros=0
	for numlibro, nlibro , nautor, precio in libros:
		if nautor.lower() == autor:
			cant_libros += 1
	print(f"el autor {autor} tiene {cant_libros} libros")
	return cant_libros
while True:
	print("\nMenú de la Blibioteca:")
	print("1. Mostrar biblioteca")
	print("2. Agregar libro")
	print("3. Cantidad de libros de un autor")
	print("4. Salir")
	opcion = input("Elija una opción (1/2/3/4): ").strip()
	if opcion == '1':
		mostrar_biblioteca()
	elif opcion == '2':
		agregar_libro_arch_bin()
	elif opcion == '3':
		cantidad_libros_autor()
	elif opcion == '4':
		break
	else:
		print("Opción no válida. Por favor, elija una opción válida (1/2/3/4).")
print("¡Adiós!")