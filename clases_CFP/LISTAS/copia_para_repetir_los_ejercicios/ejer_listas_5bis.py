lista_a = []
lista_b = []

# Leer los 10 números enteros para la lista A.
print("Ingresa los 10 números para la lista A:")
for i in range(10):
    num_a = int(input(f"Ingresa el número {i + 1} para la lista A: "))
    lista_a.append(num_a)

# Leer los 10 números enteros para la lista B.
print("Ingresa los 10 números para la lista B:")
for i in range(10):
    num_b = int(input(f"Ingresa el número {i + 1} para la lista B: "))
    lista_b.append(num_b)

# Crear una tercera lista para mezclar los números.
lista_resultante = []

# Mezclar las listas A y B intercalando los elementos.
for i in range(10):
    lista_resultante.append(lista_a[i])
    lista_resultante.append(lista_b[i])

# Imprimir la lista resultante.
print("Lista resultante después de mezclar:")
print(lista_resultante)
