# creando diccionarios con dict()  +  CON esta forma, podemos crear diccionarios VACIOS
diccionario = dict (nombre ='lucas', apellido = 'dalto')

#las listas no pueden ser claves y usamos frozenset para meter conjuntos
diccionario = {frozenset(["dalto", "rancio"]):"jajas"}

#creando diccionarios con fromkeys() valor por defecto: none
diccionario = dict.fromkeys(["nombre", "apellido"]) 

#creando diccionarios con fromkeys() cambiando el valor por defecto 'no se'
diccionario = dict.fromkeys (['nombre', 'apellido'], 'no lo se')

print (diccionario)