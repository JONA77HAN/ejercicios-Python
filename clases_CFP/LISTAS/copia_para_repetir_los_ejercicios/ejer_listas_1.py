# Ejercicio 1:  
# Leer 5 números, guardarlos en una lista y mostrarlos en el mismo orden introducido.

#print(lista[0])
#print(lista[1])
#print(lista[2])
#print(lista[3])
#print(lista[4])

lista = []

for i in range(5):
    num = int(input('ingrese su numero: '))
    lista.insert(i, num)
print(lista)    

print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
print(lista[4])