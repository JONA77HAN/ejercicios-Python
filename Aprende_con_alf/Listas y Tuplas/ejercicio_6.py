# Ejercicio 6
# Escribir un programa que almacene las asignaturas de un curso 
# (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, 
# pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista 
# las asignaturas aprobadas. Al final el programa debe mostrar por pantalla las asignaturas 
# que el usuario tiene que repetir.

asignaturas = [ 'Matemáticas', 'Física', 'Química', 'Historia' , 'Lengua']
notas = []

for nota in asignaturas:
    nota = int(input(f'¿que nota sacaste en {nota}: '))
    notas.append(nota)
    print(notas)

for i in range(len(asignaturas)):
    print(f'En {asignaturas[i]} sacaste {notas[i]}')
    


