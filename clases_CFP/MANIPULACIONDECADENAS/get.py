diccionario = {'manzana': 5, 'banana': 3, 'naranja': 2}
cantidad_manzanas = diccionario.get('manzana', 0)  # Devuelve 5, ya que 'manzana' existe en el diccionario
cantidad_uvas = diccionario.get('uva', 0)  # Devuelve 0, ya que 'uva' no existe en el diccionario
cantidad_peras = diccionario.get('pera', 'no hay mas')  # Devuelve None, ya que 'pera' no existe en el diccionario y no se proporcionó un valor predeterminado

print('quedan ' + str(cantidad_manzanas) + ' manzanas')
print(cantidad_uvas)
print(cantidad_peras)

dic = {'rojo':'amor', 'verde':'esperanza', 'amarillo':'cho'}

print(dic.get('rojo'))