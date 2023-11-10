#Ejercicio5. Escribir un programa que implemente una agenda. En la agenda se podrán guardar nombres y números de teléfono.
#El programa nos dará el siguiente menú:
#Listar: Nos muestra todos los contactos de la agenda.
#Borrar: Nos pide un nombre y si existe nos preguntará si queremos borrarlo de la agenda.
#Añadir/modificar: Nos pide un nombre. Si el nombre se encuentra en la agenda, debe mostrar el teléfono y, opcionalmente, permitir modificarlo si no es correcto. Si el nombre no se encuentra, debe permitir ingresar el teléfono correspondiente.
#Buscar: Nos pide una cadena de caracteres, y nos muestras todos los contactos cuyos nombres comiencen por dicha cadena.
#Implementar el programa con un diccionario.
from misFunciones import limpiarPantalla
agenda = {}  # Diccionario para almacenar los contactos
def listar_contactos(): 
	if not agenda:
				print("La agenda está vacía.")
	else:
				print("Lista de contactos en la agenda:")
				for nombre, telefono in agenda.items():#Nombre:Telefono
						print(f"{nombre}: {telefono}")
def borrar_contacto(nombre):
		if nombre in agenda:
				confirmacion = input(f"¿Desea borrar el contacto {nombre}? (S/N): ").strip().lower()
				if confirmacion == 's':
						del agenda[nombre]
						print(f"El contacto {nombre} ha sido borrado.")
				else:
						print(f"No se ha borrado el contacto {nombre}.")
		else:
				print(f"El contacto {nombre} no se encuentra en la agenda.")
def agregar_modificar_contacto(nombre):
		if nombre in agenda:
				print(f"Nombre: {nombre}")
				print(f"Teléfono actual: {agenda[nombre]}")
				modificar = input("¿Desea modificar el teléfono? (S/N): ").strip().lower()
				if modificar == 's':
						telefono = input("Nuevo número de teléfono: ")
						agenda[nombre] = telefono
						print(f"El teléfono del contacto {nombre} ha sido actualizado.")
				else:
						print("No se ha modificado el teléfono.")
		else:
				telefono = input("Número de teléfono: ")
				agenda[nombre] = telefono
				print(f"El contacto {nombre} ha sido agregado a la agenda.")
def buscar_contacto(cadena):
		print(f"Contactos cuyos nombres comienzan con '{cadena}':")
		for nombre in agenda.keys():
				if nombre.lower().startswith(cadena):
						print(f"{nombre}: {agenda[nombre]}")
while True:
	print("\nMenú de la Agenda:")
	print("1. Listar contactos")
	print("2. Borrar contacto")
	print("3. Añadir/Modificar contacto")
	print("4. Buscar contactos")
	print("5. Salir")
	opcion = input("Elija una opción (1/2/3/4/5): ").strip()
	limpiarPantalla()
	if opcion == '1':
		listar_contactos()
	elif opcion == '2':
		nombre = input("Nombre del contacto a borrar: ")
		borrar_contacto(nombre)
	elif opcion == '3':
		nombre = input("Nombre del contacto: ")
		agregar_modificar_contacto(nombre)
	elif opcion == '4':
		cadena = input("Introduce una cadena de búsqueda: ").lower()
		buscar_contacto(cadena)
	elif opcion == '5':
		break
	else:
		print("Opción no válida. Por favor, elija una opción válida (1/2/3/4/5).")

print("¡Adiós!")