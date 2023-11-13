
# El método setdefault() 
# El método setdefault() acepta 2 argumentos, el primero para buscar una clave en el diccionario 
# y el segundo para asignarle un valor si esa clave no existe. De esta manera, podemos en una sola 
# línea de código, crear una clave solo si no existe y asignarle un valor. 
spam = {'nombre': 'Pooka', 'edad': 5} 
spam.setdefault('color', 'negro') 
spam 
spam.setdefault('color', 'blanco') 
spam