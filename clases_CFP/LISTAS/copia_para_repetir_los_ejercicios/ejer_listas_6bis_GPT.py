# Leer 10 números enteros por teclado y almacenarlos en una lista.
numeros = []
for i in range(10):
    num = int(input(f'Ingresa el número {i + 1}: '))
    numeros.append(num)

# Verificar si la lista está ordenada de forma creciente.
creciente = sorted(numeros) == numeros

# Verificar si la lista está ordenada de forma decreciente.
decreciente = sorted(numeros, reverse=True) == numeros

# Determinar el resultado.
if creciente:
    print('La lista está ordenada de forma creciente.')
elif decreciente:
    print('La lista está ordenada de forma decreciente.')
else:
    print('La lista está desordenada.')
