ingreso_mensual = 80000
gasto_mensual = 40000

#if anidados  

if ingreso_mensual > 10000:
    if ingreso_mensual - gasto_mensual < 0:
        print ('estas en deficit')
    elif ingreso_mensual - gasto_mensual > 3000:
        print ('estas bien') 
    else:       
        print('estas bien en cualquier parte del mundo')

elif ingreso_mensual > 1000:
    print('estas bien en lationoamerica')

elif ingreso_mensual > 500:
    print('estas bien en Argentina') 

elif ingreso_mensual > 200:
    print('estas bien en Venezuela')

else: 
    print ('sos pobre')



dinero_billetera = 2100

if dinero_billetera > 4000:
    print('buenisimo, vamo al cine')
elif dinero_billetera > 3500:
    print('vamos a comer a Mac')
elif dinero_billetera > 2500:
    print ('vamo a comer a Mac solo ustedes')
elif dinero_billetera > 2000:
    print ('vamos a la plaza')
else:
    print ('hola argentina ')            












