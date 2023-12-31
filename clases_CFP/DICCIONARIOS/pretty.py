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