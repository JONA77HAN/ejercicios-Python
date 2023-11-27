# Ejercicio 9
# Escribir un programa que pregunte al usuario la fecha de su nacimiento 
# en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. 
# Adaptar el programa anterior para que también funcione cuando el día o 
# el mes se introduzcan con un solo carácter.

fecha = input("Introduce la fecha de tu nacimiento en formato día/mes/año: ")
dia = fecha[:fecha.find('/')]
print(f'El dia es {dia}')
mesAño = fecha[fecha.find('/')+1:]

mes = mesAño[:mesAño.find('/')]
print(f'El mes es {mes}')

año = mesAño[mesAño.find('/')+1:]
print(f'El año es {año}')