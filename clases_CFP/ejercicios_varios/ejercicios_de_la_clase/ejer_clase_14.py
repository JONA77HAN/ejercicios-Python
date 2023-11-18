# Ejercicio14. 
# Dadas las edades y alturas de 5 alumnos 
# Mostrar la edad y la estatura promedio 
# La cantidad de alumnos mayores de 18 años 
# Y la cantidad de alumnos que miden más de 175cm.

from random import randint

edad_promedio = 0
mayor_de_edad = 0
suma_edad = 0
suma_altura = 0

for i in range(5):
    edad_alumn = randint(15,20)
    altura_alumn = randint(150,185)
    print( 'edad: ' + str(edad_alumn) + ' años')  
    print( 'altura: ' + str(altura_alumn) + ' cm' )  
    if edad_alumn >= 18:
        mayor_de_edad += 1 
    suma_edad += edad_alumn
    suma_altura+= altura_alumn

promedio_edad = suma_edad / 5
promedio_altura = suma_altura / 5

print('-----------------------------------------------')
print ('la altura promedio de los alumnos es ' + str(promedio_altura))   
print ('Y la edad promedio es ' + str(promedio_edad))    
print (str(mayor_de_edad) + ' son mayores de edad')