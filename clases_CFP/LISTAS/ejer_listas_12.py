# Ejercicio 12: 
# Queremos desarrollar una aplicación que nos ayude a gestionar las notas de un centro educativo. 
# Cada grupo (o clase) está compuesto por 5 alumnos. 
# Se pide leer las notas del primer, segundo y tercer trimestre de un grupo. 
# Debemos mostrar al final: 
# la nota promedio del grupo en cada trimestre, 
# y el promedio del alumno que se encuentra en la posición N (N se lee por teclado).

#Ejemplo de Lista:
#libroNotas = [[6,8,5],[8,7,9],...,[6,6,6]]
def calcular_promedio(trimestre):
    total = sum(trimestre)
    return total / len(trimestre)

def main():
    num_alumnos = 5
    num_trimestres = 3

    # Inicializar una lista vacía para almacenar las notas de todos los alumnos
    libro_notas = []

    # Leer las notas para cada alumno y cada trimestre
    for i in range(num_alumnos):
        notas_alumno = []
        for j in range(num_trimestres):
            nota = float(input(f"Ingrese la nota del alumno {i + 1} en el trimestre {j + 1}: "))
            notas_alumno.append(nota)
        libro_notas.append(notas_alumno)

    # Calcular el promedio del grupo en cada trimestre
    promedios_trimestres = [calcular_promedio([notas[i] for notas in libro_notas]) for i in range(num_trimestres)]

    # Mostrar los promedios de cada trimestre
    for i, promedio in enumerate(promedios_trimestres):
        print(f"Promedio del trimestre {i + 1}: {promedio}")

    # Calcular el promedio del alumno en una posición específica (N)
    n = int(input("Ingrese la posición del alumno cuyo promedio desea calcular (1-5): ")) - 1

    if 0 <= n < num_alumnos:
        promedio_alumno_n = calcular_promedio(libro_notas[n])
        print(f"Promedio del alumno en la posición {n + 1}: {promedio_alumno_n}")
    else:
        print("La posición ingresada no es válida.")

if __name__ == "__main__":
    main()
