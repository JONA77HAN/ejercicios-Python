animales = ['gato', 'perro', 'loro', 'cocodrilo']
numeros = [10, 20, 55, 90]

#recorriendo la lista animales
for animal in animales :
    animal = + f'a cada paso uno'
    print ( f'ahora la variable es igual a : {animal}')

#recorriendo la lista num y multiplicando por 10
for numero in numeros:
    resultado = numero * 10
    print(resultado)

#iterando dos listas del mismo tamaño al mismo tiempo con la funcion zip
for numero, animal in zip (animales, numeros):
    print(f'recorriendo la lista 1: {numero}')
    print(f'tambien la lista 2 : {animal}')

#forma correcta de recorrer una lista con su indice
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1] 
    print (f'el indice es : {indice} y el valor es : {valor}')   

#usando el for/else
for numero in numeros:
    print (f' ejecutando el ultimo bucle, valor actual : {numero}')
else:
    print ('el bucle termino.')    

#todo esto funciona exactamente igual para tuplas, listas y conjuntos

