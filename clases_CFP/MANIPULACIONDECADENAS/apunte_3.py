# Métodos startswith(), endswith() y find()
# Los métodos startswith() u endswith() devuelven un booleano True o False si la cadena 
# empieza o termina, respectivamente, con el argumento que le pasamos.

# El método find() funciona de manera similar, nos permite buscar en un rango de la cadena en 
# particular y devolverá -1 si no lo encuentra o la posición donde se encontró la cadena.

ejemplo = 'todas las flores son rojas, todo el rojo no es flor'.find('no')
print(f'la palabra "no" esta en la posicion {ejemplo}')


