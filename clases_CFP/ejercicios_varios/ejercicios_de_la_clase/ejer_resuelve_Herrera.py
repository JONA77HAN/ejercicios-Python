facturacion_total=0
ltr_art_1=0
fact_may_600=0

for i in range(5):

  cod_art=int(input('Ingrese el codigo de articulo: \n')) #+str(i+1)
  
  precio_ltr=int(input('Ingrese el precio por litro: \n'))
  
  cant_x_ltr=int(input('Ingrese la cantidad vendida en litros: \n')) #+str(i+1)

costo_fact = cant_x_ltr * precio_ltr
facturacion_total = facturacion_total + costo_fact

if costo_fact > 600 :
  fact_may_600 = fact_may_600 + 1

if cod_art == 1 :
  ltr_art_1 = ltr_art_1 + cant_x_ltr

print('1-Facturacion Total:$'+' '+str(facturacion_total))
#print(f'1-Facturacion Total: ${facturacion_total}')

print('2-Cantidad de litros del articulo 1: '+' '+str(cant_x_ltr))
#print(f'2-Cantidad de litros del articulo 1:{cant_x_ltr} ')

print('3-Cantidad de facturas de mas de $600:'+' '+str(fact_may_600))

#print(f'3-Cantidad de facturas de mas de 600: {fact_may_600}')