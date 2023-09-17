# Ejercicio16.
# Una empresa que se dedica a la venta de desinfectantes necesita un programa para gestionar las facturas. 
# En cada factura figura:
# el código del artículo
# la cantidad vendida en litros
# y el precio por litro.
# Se pide de 5 facturas introducidas:
# Facturación total,
# cantidad en litros vendidos del artículo 1
# y cuantas facturas se emitieron de más de $600.

#Ejemplo
#5
#60
#$40
#60*40 -> subtotal

from random import randint

facturacion_total = 0
litros_vendidos_art_uno = 0
facturas_mas_de_seis = 0

for i in range(5):
    codigo_del_articulo = randint(1,10)
    litros_vendidos = randint(10,50)
    litros_precio = randint(15,30)
    subtotal = litros_precio * litros_vendidos
    print ('Articulo n°' + str(codigo_del_articulo) + ' -----> '+ str(litros_vendidos) + ' litros a $ ' + str(litros_precio) +'.- subtotal de $'+str(subtotal) + '.-'  )
    facturacion_total += subtotal
    if codigo_del_articulo == 1:
        litros_vendidos_art_uno += litros_vendidos 
    if subtotal >= 600:
        facturas_mas_de_seis += 1    

print ( 'La facturacion total es de $' + str(facturacion_total) + '.-' )

if litros_vendidos_art_uno > 0:
    print ( 'Del articulo "1" se vendieron ' + str(litros_vendidos_art_uno) + ' litros')
else:
    print ('El articulo "1" no registro ventas')

if facturas_mas_de_seis > 0:
    print ('Se emitieron ' + str(facturas_mas_de_seis) + ' facturas superiores a $600.-')
else:
    print ('No se registraron facturas mayores a $600.-')    



