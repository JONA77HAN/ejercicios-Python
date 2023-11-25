# Ejercicio 1
# Escribir un programa que pregunte el nombre del usuario en la 
# consola y un número entero e imprima por pantalla en líneas distintas 
# el nombre del usuario tantas veces como el número introducido.

nombre = input('Ingrese su nombre: ')
cantidad = int(input('Ingrese la cantidad de veces q quiere q aparezca su nombre: '))

for i in range(cantidad):
    print(nombre)

# Solucion Alf
nombre = input("¿Cómo te llamas? ")
n = input("Introduce un número entero: ")
print((nombre + "\n") * int(n))    