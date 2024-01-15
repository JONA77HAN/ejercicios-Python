# Ejercicio 1
# Escribir un programa que almacene las asignaturas de un curso 
# (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una 
# lista y la muestre por pantalla.

lista = []
materia =''

while materia != 'stop':
    materia = input('Ingresa la materia: ')
    lista.append(materia)
    print(lista)

