# Ejercicio13 
# Pedir 10 sueldos 
# Mostrar su suma y cuantos hay mayores de $1000 
# Y decir cual fue el sueldo más alto.

from random import randint

c = 0
suma_sueldos = 0
mas_de_mil = 0
menos_de_mil = 0

for i in range(10):
    sueldo = randint(500,1500)
    if sueldo > 1000:
        mas_de_mil += 1
    else:
        menos_de_mil += 1
suma_sueldos += sueldo



print(f'---> la suma de todos los sueldos es {suma_sueldos}')
print(f'---> {mas_de_mil} eran mayores a mil')


