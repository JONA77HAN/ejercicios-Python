from random import randint

c = 0
suma_sueldos = 0
mas_de_mil = 0
menos_de_mil = 0
sueldo_maximo = 0  # Inicializa la variable para el sueldo más alto

for i in range(10):
    sueldo = randint(500, 1500)
    suma_sueldos += sueldo  # Agrega el sueldo actual al total

    if sueldo > 1000:
        mas_de_mil += 1
    else:
        menos_de_mil += 1

    if sueldo > sueldo_maximo:
        sueldo_maximo = sueldo  # Actualiza el sueldo máximo si es mayor

print(f'---> la suma de todos los sueldos es {suma_sueldos}')
print(f'---> {mas_de_mil} eran mayores a mil')
print(f'---> El sueldo más alto fue: {sueldo_maximo}')
