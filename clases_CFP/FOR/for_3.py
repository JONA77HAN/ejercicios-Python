# Ejercicio10 
# Armar un programa que muestre el producto de los 10 primeros números impares.
# 1,3,5,

producto = 1

for i in range (1,21,2):
    producto = i * producto
print('el producto de los 10 primeros numeros impares es ' + str(producto))    
    