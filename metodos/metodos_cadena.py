#      =>    resultado = DATO.METODO()  un metodo, es una funcion aplicada a un Metodo

cadena1 = 'hola, soy Dalto'
cadena2 = 'Bienvenido maquinola'
cadena3 =  'texto de prueba que nos habla de la bondad en el corazon de los extraterrestres'

#convierte a mayuscula
mayusc = cadena1.upper()    

#convierte a minuscula
minusc = cadena1.lower()

#convierte la Primer letra a mayuscula
primer_letra_a_mayuscula = cadena1.capitalize()

#buscamos una cadena en otra cadena, -1 cuando no esta
busqueda_find = cadena1.find('hola')

#buscamos una cadena en otra cadena, si no hay coincidencias lanza una excepcion
busqueda_index = cadena1.index('s')

#si es numerico devolvemos true
es_numerico = cadena1.isnumeric()

#si es alfanumerico decolvemos True
es_alfanumerico = cadena1.isalpha()

#contamos las coincidencias de una cadena dentro de otra cadena, devuelve la cantidad de veces que coincidencias
contar_coincidencias = cadena1.count('hola')

#contamos cuantos caracteres tiene una cadena
contar_caracteres = len(cadena1)    #es una funcion, no un metodo.

#verificamos si una cadena empieza con otra cadena dada, si es asi devuelve True.
empieza_con = cadena1.startswith ('H')

#verificamos si una cadena termina con otra cadena dada, si es asi devuelve True.
empieza_con = cadena1.endswith ('H')

#si el valor 1 se encuentra en la cadena original, reemplaza el valor 1 de la misma, por el valor 2.
cadena_nueva = cadena1.replace('hola', 'Roberto')

#separar cadenas con la cadena que le pasemos
cadena_separada = cadena1.split(" ")

#print (cadena1)  

cadena4 = cadena3.split()
print(f' ahora deberia aparecer esta : {cadena4} y acontecer todo lo demas')