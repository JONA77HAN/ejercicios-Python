# La función list(spam.keys) toma los valores de la dict_key y los devuelve en forma de lista. 
# Podemos utilizar el truco de asignación múltiple en un ciclo for para asignar la clave y el valor a 
# distintas variables. 
piezas_blancas = {
    'peon' : 1,
    'caballo' : 3,
    'alfil' : 3,
    'torre' : 5,
    'reina' : 9,
    'rey' : 4
}

print(piezas_blancas.items())
print(piezas_blancas.values())
print(piezas_blancas.keys())