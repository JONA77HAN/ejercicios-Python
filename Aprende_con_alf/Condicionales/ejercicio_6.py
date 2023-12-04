# Ejercicio 6
# Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al 
# sexo y el nombre. El grupo A esta formado por las mujeres con un nombre 
# anterior a la M y los hombres con un nombre posterior a la N y el grupo B
# por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, 
# y muestre por pantalla el grupo que le corresponde.

grupo_a = []#mujeres nombre (a,b,c,d,e,f,g,h,i,j,k,l,m)y hombres(n,o,p,q,r,s,t,u,v,w,x,y,z)
grupo_b = []#el resto

nombre = input('Ingrese su nombre: ')
sexo = input('Ahora ingrese su sexo (f/m): ')

if nombre.lower() < 'm' and sexo == 'f' or nombre.lower() < 'n' and sexo == 'm':
    grupo_a.append(nombre)
else:
    grupo_b.append(nombre)

print(grupo_a)
print(grupo_b)

