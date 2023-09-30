# Ejercicio 2: 
# Leer 5 números: guardarlos en una lista y mostrarlos en orden inverso al introducido.

lista = []

# leo 5 numeros y los guardo en una lista
for i in range(5):
    num = int(input('ingrese su numero: \n -----> '))
    lista.insert(i, num)
print(lista)

