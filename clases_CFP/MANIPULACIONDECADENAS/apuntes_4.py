"""
Métodos join() y split():
Los métodos join() y split() nos sirven a la hora de unir listas de cadenas. El método join() se 
llama en una cadena y toma como argumento una lista con valores string que se concatenaran
con la cadena separándolos. Por el otro lado el método split() devuelve una lista de cadenas 
donde cada valor serán las palabras de la cadena, por defecto los espacios en blanco se utilizan 
para delimitarlas.
"""
print('JOIN: ')
print(' '.join(['hermosas', 'aromáticas', 'coloridas' ,'bellas']))
print(' las flores '.join(['hermosas', 'aromáticas', 'coloridas' ,'bellas']))
print(' * '.join(['Mi', 'nombre', 'es', 'Simon']))
print('-'*50)
print('SPLIT:')
print('Mi nombre es Leon Benjamin Carranza'.split('m'))
print('MiABCnombreABCesABCSimon'.split('ABC'))
print('MinombreesSimon'.split('m'))

print('rarisimo eso que esta sucediendo'.split())

