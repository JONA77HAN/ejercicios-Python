#metodos q ultizamos con diccionario
#key
#get


diccionario = {
    "nombre": 'lucas',
    "apellido": 'dalto',
    "subs": 1000000
}

#nos devuelve un objeto dict_item
claves = diccionario.keys()


#obtendiendo un elemento con get() (si no encuentra nada el programa continua)
valor_de_kolokk = diccionario.get('kolokk')
print('el programa continua')

#eliminando todo del diccionario
#diccionario.clear()

#eliminando un elemento del diccionario
diccionario.pop('nombre')

#obteniendo un elemento dict_items iterable
diccionario_iterable = diccionario.items()


