# Ejercicio8. Continuando el ejercicio7, agregar un menu para mostrar la agenda completa, 
# cargar un contacto nuevo, modificarlo o borrarlo.

from misFunciones import limpiarPantalla
dirAgenda = './agenda.txt'

def listar_agenda(dirAgenda):
  arcAgenda = open(dirAgenda)
  contAgenda = arcAgenda.readlines()
  arcAgenda.close()
  listaAgenda = []
  for linea in contAgenda:  
    listaInfo = linea.split(';')
    contacto = {'id':'','nombre':'' ,'apellido':'','nac':''}
    for clave in contacto:
      contacto[clave]=listaInfo.pop(0)
    listaAgenda.append(contacto)
  for contacto in listaAgenda:
    print(f'ID {contacto["id"]}'.center(30,'='))
    print('Nombre'.ljust(15,'.')+contacto["nombre"].rjust(15,'.'))
    print('Apellido'.ljust(15,'.')+contacto["apellido"].rjust(15,'.'))
    print('Nacimiento'.ljust(15,'.')+contacto["nac"].rjust(15,'.'))
def borrar_contacto_agenda(dirAgenda):
	arcAgenda = open(dirAgenda)
	contAgenda = arcAgenda.readlines()
	arcAgenda.close()
	idBorrar = input('id que quiere borrar ')
	for i in range(len(contAgenda)):
		if contAgenda[i].split(';')[0] == idBorrar:
			del contAgenda[i]
			break
	cadenaAgenda = ''
	for contacto in contAgenda:
		cadenaAgenda += contacto
	cadenaAgenda = cadenaAgenda.strip('\n')
	print(cadenaAgenda)
	arcAgenda = open(dirAgenda, 'w')
	arcAgenda.write(cadenaAgenda)
	arcAgenda.close()

def modificar_contacto_agenda(dirAgenda):
	arcAgenda = open(dirAgenda)
	contAgenda = arcAgenda.readlines()
	arcAgenda.close()
	idMod = int(input('ingrese id '))
	for i in range(len(contAgenda)):
		if contAgenda[i].split(';')[0] == idMod:
			nacMod = input('ingrese fecha de nacimiento ')+'\n'
			contMod = ';'.join(contAgenda[i].split(';')[:-1].append(nacMod))
			print(contMod)
			break
	input()	
	cadenaAgenda = ''
	for contacto in contAgenda:
		cadenaAgenda += contacto
	cadenaAgenda = cadenaAgenda.strip('\n')
	print(cadenaAgenda)
	arcAgenda = open(dirAgenda, 'w')
	arcAgenda.write(cadenaAgenda)
	arcAgenda.close()
        
def añadir_contacto_agenda(dirAgenda):
  arcAgenda = open(dirAgenda)
  contAgenda = arcAgenda.readlines()
  arcAgenda.close()
  id = input('ingrese id ')
  nombre = input('ingrese nombre ')
  apellido = input('ingrese apellido ')
  fechadenac = input('ingrese fecha de nacimiento ')
  contactoAñadir = str(id)+';'+nombre+';'+apellido+';'+fechadenac+'\n'

  archAgenda = open('agenda.txt', "a")  
  archAgenda.write(contactoAñadir)
  archAgenda.close()
while True:
	limpiarPantalla()
	print("\nMenú de la Agenda:")
	print("1. Listar contactos")
	print("2. Borrar contacto")
	print("3. Añadir contacto")
	print("4. Modificar contactos")
	print("5. Salir")
	opcion = input("Elija una opción (1/2/3/4/5): ")[0]
	if opcion == '1':
		listar_agenda(dirAgenda)
	elif opcion == '2':
		borrar_contacto_agenda(dirAgenda)
	elif opcion == '3':
		añadir_contacto_agenda(dirAgenda)
	elif opcion == '4':
		modificar_contacto_agenda(dirAgenda)
	elif opcion == '5':
		break
	else:
		print("Opción no válida. Por favor, elija una opción válida (1/2/3/4/5).")
	input()
print("¡Adiós!")