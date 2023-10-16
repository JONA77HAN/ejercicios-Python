        # El método get() 
# Para no tener que prevenir los errores de no encontrar una clave dentro de un diccionario existe 
# el método get(). Este método toma 2 argumentos: la clave del valor que estamos buscando, y el 
# valor que devolverá en caso de no encontrarlo.  
elementosPicnic = {'manzanas': 5, 'vasos': 2} 
'Yo voy a traer ' + str(elementosPicnic.get('vasos', 0)) + ' vasos.' 
'Yo voy a traer ' + str(elementosPicnic.get('huevos', 0)) + ' huevos.' 
elementosPicnic = {'manzanas': 5, 'vasos': 2} 
'Yo voy a traer' + str(elementosPicnic['huevos']) + ' huevos.' 
 
        # El método setdefault() 
# El método setdefault() acepta 2 argumentos, el primero para buscar una clave en el diccionario 
# y el segundo para asignarle un valor si esa clave no existe. De esta manera, podemos en una sola 
# línea de código, crear una clave solo si no existe y asignarle un valor. 
spam = {'nombre': 'Pooka', 'edad': 5} 
spam.setdefault('color', 'negro') 
spam 
spam.setdefault('color', 'blanco') 
spam

        # Pretty Printing 
# Existe un módulo o librería llamada Pretty Printing que nos puede ayudar a mostrar nuestros 
# diccionarios en pantalla. Pretty Printing nos da acceso a las funciones pprint() y pformat() para 
# lograr esto. 
  
import pprint 
mensaje = 'Era un día frio de abril, cuando dieron las 12' 
contar = {} 
for caracter in mensaje: 
    contar.setdefault(caracter, 0) 
    contar[caracter] = contar[caracter] + 1 
pprint.pprint(count) 
 
# SI en lugar de imprirlo directamente por pantalla queremos utilizar la string para algo más, se 
# puede utilizar pformat() 
 
print(pprint.pformat(contar)) 