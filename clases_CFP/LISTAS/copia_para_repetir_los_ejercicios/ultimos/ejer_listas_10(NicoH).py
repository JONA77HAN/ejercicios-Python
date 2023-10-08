# Ejercicio 10: 
# Leer 10 enteros: 
# Guardar en otra lista los elementos pares de la primera, 
# y a continuación los elementos impares.
# Ejercicio10. Leer 10 enteros. Guardar en otra lista los elementos pares de la primera, y a continuación los elementos impares.
# listaA = [1,2,3,4,5,6,7,8,9,10]
# Resultado: listaB = [2,4,6,8,10,1,3,5,7,9]

libroNotas = [[6,8,5],[8,7,9],[9,8,10],[3,6,8],[6,6,6]]
sumaTrimestres = [0,0,0]
sumaTrimAlumno = 0
promTrimestres = [0,0,0]

for t in range(3):
  for i in range(5):
    sumaTrimestres[t] += libroNotas[i][t]  

posicion = int(input('ingrese posicion del alumno '))
for i in range(3):
  sumaTrimAlumno += libroNotas[posicion][i]
  promTrimestres[i] = round(sumaTrimestres[i]/5,2)

promTrimAlumno = sumaTrimAlumno/3

print('el promedio del primer trimestre es ' + str(promTrimestres[0]))
print('el promedio del segundo trimestre es ' + str(promTrimestres[1]))
print('el promedio del tercer trimestre es ' + str(promTrimestres[2]))

print('el promedio del alumno es ' + str(promTrimAlumno))


