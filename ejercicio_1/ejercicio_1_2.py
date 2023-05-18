#le pedimos al usuario q nos diga una frase o varias
frase = input ("Decime una frase y te caluclo cuanto tardarias si tuvieras que decirla: ")

#creamos una lista con todas las palabras de la frase ( se separan cada vez q hay un espacio en blanco )
palabras_separadas = frase.split(" ")

#usamos len() para ver la cantidad de elementos q hay en la lista
cantidad_de_palabras = len(palabras_separadas)

#en caso de q tarde mas de un minuto le decimos q pare la onda
if cantidad_de_palabras > 120:
    print('para flaco, no te pedi un testamento')

#calculamos cuanto tadaria en decir las palabras y se lo decimos
print(f'Dijiste {cantidad_de_palabras} palabras, tardarias {cantidad_de_palabras/2} segundos en decirlo ')
print (f'Dalto lo diria en {cantidad_de_palabras * 100 // 2 *1.3 / 100} segundos')
