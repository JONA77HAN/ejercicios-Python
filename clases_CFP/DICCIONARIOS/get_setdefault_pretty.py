#El método get() 
# Para no tener que prevenir los errores de no encontrar una clave dentro de un diccionario existe 
# el método get(). Este método toma 2 argumentos: la clave del valor que estamos buscando, y el 
# valor que devolverá en caso de no encontrarlo.  
elementosPicnic = {'manzanas': 5, 'vasos': 2} 
'Yo voy a traer ' + str(elementosPicnic.get('vasos', 0)) + ' vasos.' 
'Yo voy a traer ' + str(elementosPicnic.get('huevos', 0)) + ' huevos.' 
elementosPicnic = {'manzanas': 5, 'vasos': 2} 
'Yo voy a traer' + str(elementosPicnic['huevos']) + ' huevos.' 
 
