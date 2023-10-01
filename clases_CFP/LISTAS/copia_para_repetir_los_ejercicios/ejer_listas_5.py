# Ejercicio5
# Leer por teclado dos listas de 10 números enteros 
# y mezclarlas en una tercera de la forma: el 1º de A, el 1º de B, el 2º de A, el 2º de B, etc.
from random import randint
lista_a = []
lista_b = []
lista_mezcla = []
for i in range(10):
    num = randint(0, 100)
    lista_a.append(num)
for i in range(10):
    num = randint(0, 100)
    lista_b.append(num)
print('Lista "a" ---> ' + str(lista_a))
print('Lista "b" ---> ' + str(lista_b))
print('-'*50)
print('La siguiente lista es una mezcla de la "a" y la "b" ')
for i in range(5):
    lista_mezcla.append(lista_a[i])
    lista_mezcla.append(lista_b[i])
print('la lista mezcla quedó de la siguiente forma ---> ' + str(lista_mezcla))    
