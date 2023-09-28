# Ejercicio5
# Leer por teclado dos listas de 10 números enteros 
# y mezclarlas en una tercera de la forma: el 1º de A, el 1º de B, el 2º de A, el 2º de B, etc.

lista_a = []
lista_b = []
c_a = 0
c_b = 0

for i in range(10):
    num_a = int(input('ingrese un numero para la lista_a : '))
    c_a += 1
    lista_a.insert(c_a, num_a)

for f in range(10):
    num_b = int(input('ingrese un numero para la lista_b : '))
    c_b += 1
    lista_b.insert(c_b, num_b)

print(lista_a)
print(lista_b)

lista_mezcla = []

for i in range(10):
    lista_mezcla.append(lista_a[i])
    lista_mezcla.append(lista_b[i])

print(lista_mezcla)



#num_b = int(input('ingrese un numero para la lista_b : '))

