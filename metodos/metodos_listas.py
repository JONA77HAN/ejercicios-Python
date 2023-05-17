#creand una lista con list()
lista = list(['hola','como','va', 'todo','esta','bien'])

#devuelve la cantidad de elemtentos de la lista
cantidad_elementos = len(lista)

#agregando un elemento a la lista
lista.append('jajajaja')

#agregando un elemento a la lista en un indice especifico
lista.insert(2,'toma la leche')

#agregando varios elementos a la lista
lista.extend([False, 2030])

#eliminando un elemento de la lista (por su indice)
lista.pop(3) #-1 para eliminar el ultimo, -2 para eliminar el anteultimo y asi sucesivamente

#elimina todos los elementos de la lista
#lista.clear()

#ordenando la lista de forma ascendente (si usamos el parametro reverse=True lo ordena en reversa)
lista.sort() #deben ser datos numericos, tmb True o False

#invierte los elementos de una lista
lista.reverse()

#verificando si un elemento esta en la lista
elemento_encontrado = lista.index()



#