# Ejercicio 12
# Una panadería vende barras de pan a 3.49€ cada una. 
# El pan que no es el día tiene un descuento del 60%. 
# Escribir un programa que comience leyendo el número de barras vendidas
# que no son del día. Después el programa debe mostrar el precio 
# habitual de una barra de pan, el descuento que se le hace por no ser fresca 
# y el coste final total.

cant_barras_pan_viejo = int(input('Ingrese cuantas barras de pan viejas vendiste hoy: '))
precio_sin_descuento = round(cant_barras_pan_viejo * 3.49, 2)
print(f'Su compra serian ${precio_sin_descuento}.-')
descuento = precio_sin_descuento * 60 / 100
precio_final = precio_sin_descuento - descuento
print(f'Pero con el descuento de pan viejito.\nLa compra le queda en ${precio_final}.-')