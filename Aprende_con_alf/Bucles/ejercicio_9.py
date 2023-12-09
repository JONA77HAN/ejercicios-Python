# Ejercicio 9
# Escribir un programa que almacene la cadena de caracteres contraseña en una 
# variable, pregunte al usuario por la contraseña hasta que introduzca 
# la contraseña correcta.

contraseña = 'Lucy4903'
passw = ''
while True:
    passw = input('Ingrese la contraseña: ')
    if passw == contraseña:
        print('Acceso Autorizado')
        break
    else:
        print('ERROR')    

"""
while contraseña != passw:
    passw = input('Ingrese la contraseña: ')
    print('ERROR')
print('Acceso Autorizado')
"""