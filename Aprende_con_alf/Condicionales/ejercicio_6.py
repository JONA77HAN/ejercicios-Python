# Ejercicio 6
# Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al 
# sexo y el nombre. El grupo A esta formado por las mujeres con un nombre 
# anterior a la M y los hombres con un nombre posterior a la N y el grupo B
# por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, 
# y muestre por pantalla el grupo que le corresponde.
grupo_a = []
grupo_b = []

def obtener_grupo(nombre, sexo):
    if (sexo == 'f' and nombre < 'M') or (sexo == 'm' and nombre > 'N'):
        grupo_a.append(nombre)
    else:
        grupo_b.append(nombre)
    print(grupo_a)
    print(grupo_b)

while True:
    nombre = input("Ingrese su nombre: ")
    sexo = input("Ingrese su sexo (f/m): ")
    obtener_grupo(nombre, sexo)
    opcion = input('¿Seguir? (s/n): ')
    if opcion.lower() != 's':
        break






