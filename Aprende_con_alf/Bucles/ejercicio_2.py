# Ejercicio 2
# Escribir un programa que pregunte al usuario su edad y muestre por pantalla 
# todos los años que ha cumplido (desde 1 hasta su edad).
edad = int(input('¿Cual es tu edad? '))
año = int(input('¿En que año naciste?: '))

for i in range(edad):
    print(f'En el año {año+i} has cumplido {i} años')