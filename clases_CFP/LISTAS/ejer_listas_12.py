# Ejercicio 12: 
# Queremos desarrollar una aplicación que nos ayude a gestionar las notas de un centro educativo. 
# Cada grupo (o clase) está compuesto por 5 alumnos. 
# Se pide leer las notas del primer, segundo y tercer trimestre de un grupo. 
# Debemos mostrar al final: 
# la nota promedio del grupo en cada trimestre, 
# y el promedio del alumno que se encuentra en la posición N (N se lee por teclado).

#Ejemplo de Lista:
#libroNotas = [[6,8,5],[8,7,9],...,[6,6,6]]

alumno_notas = []

# genera libro de notas aleatoriamente
from random import randint
for f in range(5):
  for i in range(3):
      nota = randint(1, 10)
      alumno_notas.append(nota)
alumno_a = alumno_notas[:3]
alumno_b = alumno_notas[3:6]
alumno_c = alumno_notas[6:9]
alumno_d = alumno_notas[9:12]    
alumno_e = alumno_notas[12:]
libro_notas = [alumno_a, alumno_d, alumno_c, alumno_d, alumno_d]
print('Libro de Notas generado automaticamente: ')
print(libro_notas)
#mostrar nota promedio de cada trimestre
suma_primer_trimestre = libro_notas[0][0] + libro_notas[1][0] + libro_notas[2][0] + libro_notas[3][0] + libro_notas[4][0]
promedio_primer_trimestre = round(suma_primer_trimestre/5, 2)
print('El promedio de los alumnos en el primer trimestre es ' + str(promedio_primer_trimestre))

suma_segundo_trimestre = libro_notas[0][1] + libro_notas[1][1] + libro_notas[2][1] + libro_notas[3][1] + libro_notas[4][1]
promedio_segundo_trimestre = round(suma_segundo_trimestre/5, 2)
print('El promedio en el segundo ' + str(promedio_segundo_trimestre))  

suma_tercer_trimestre = libro_notas[0][2] + libro_notas[1][2] + libro_notas[2][2] + libro_notas[3][2] + libro_notas[4][2]
promedio_tercer_trimestre = round(suma_tercer_trimestre/5, 2)
print('Y durante el tercer trimestre ' + str(promedio_tercer_trimestre))

# y el promedio del alumno que se encuentra en la posición N (N se lee por teclado).




    


