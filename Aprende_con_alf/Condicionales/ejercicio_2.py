# Ejercicio 2
# Escribir un programa que almacene la cadena de caracteres contraseña en 
# una variable, pregunte al usuario por la contraseña e imprima por pantalla
# si la contraseña introducida por el usuario coincide con la guardada en la 
# variable sin tener en cuenta mayúsculas y minúsculas.

contraseña = input('Cree su contraseña: \n')

while True:
    login = input('ahora ingrese la contraseña creada: \n')
    if login.lower() == contraseña.lower():
        print('Ingreso Autorizado')
        break
    else:
        print('ERROR, ingrese su clave nuevamente')
