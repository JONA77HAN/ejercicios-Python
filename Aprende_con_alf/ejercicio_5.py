#Ejercicio 5
#Escribir un programa que pregunte al usuario por el número de horas trabajadas 
#y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.
nombre = input('Hola cual es tu nombre?\n')
cant_horas = int(input(f'{nombre} decime cuantas horas por dia trabajas:\n'))
dinero_por_hora = int(input(f'y decime, cuanto cobras por hora?\n'))

ganas = cant_horas*dinero_por_hora

print(f'Osea {nombre} que te corresponden ${ganas}.- por cada dia de tu trabajo')

sueldo = ganas*20

print (f'Serian unos ${sueldo}.- por mes ')