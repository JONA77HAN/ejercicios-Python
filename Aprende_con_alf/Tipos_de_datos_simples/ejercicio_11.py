# Ejercicio 11
# Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. 
# Estos ahorros debido a intereses, que no se cobran hasta finales de año, 
# se te añaden al balance final de tu cuenta de ahorros. 
# Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, 
# introducida por el usuario. Después el programa debe calcular y mostrar por pantalla 
# la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales.

dinero_depositado = int(input('Ingrese el dinero depositado: '))
primer_año = round(dinero_depositado * 4 /100 + dinero_depositado, 2)
print(f'Para el fin del primer año tendrás ${primer_año}.-')
segundo_año = round(primer_año * 4 /100 + primer_año, 2)
print(f'Para el fin del segundo año tendrás ${segundo_año}.-')
tercer_año = round(segundo_año * 4 /100 + segundo_año, 2)
print(f'Para el fin del tercer año tendrás ${tercer_año}.-')