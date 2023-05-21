#pedirle un dato al usuario
nombre = input ('che maestro, dame tu nombre: ')

#mostrando el dato
print (nombre)

#mostrando el dato
print ( f'el nombre es: {nombre}')

color = input ('decime un color: ')
print(f'el color que elegiste es el {color}')

frutas = input ('elegi una fruta, la q mas te guste: ')
if frutas == 'manzana':
    print (f'la fruta q elegiste es mi favorita')
else:
    print (f'esta buena la {frutas} pero mi favorita es la manzana')