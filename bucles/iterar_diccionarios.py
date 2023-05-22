diccionario = {
    'nombre': 'lucas',
    'apellido': 'dalto',
    'subs' : 1000000
}

#recorriendo diccionario para obtener las claves
for key in diccionario:
    key
    print (f'la claves es: {key}')

#recorriendo diccionario con items() para obtener las claves y los valores
for datos in diccionario.items():
    key = datos [0]
    value = datos [1]
    print (f'la clave es: {key} y el valor: {value}')    