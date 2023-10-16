# Si queremos listas de estos valores se puede utilizar la función list() 

spam = {'color': 'rojo', 'edad': 42} 
spam.keys() 
print(list(spam.keys ()))
print('-'*30)

piezas_negras = {
    'peon': 1,
    'caballo': 3,
    'alfil' : 3,
    'torre' : 5,
    'reina' : 9,
    'rey' : 4
}

print(list(piezas_negras.items()))
print(list(piezas_negras.values()))
print(list(piezas_negras.keys()))


