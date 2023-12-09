# Ejercicio 13
# Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta 
# que el usuario escriba “salir” que terminará.

palabra = ''
while palabra != 'salir':
    palabra = input('introduce una palabra: ')
    print(palabra)
print('saliste!')    