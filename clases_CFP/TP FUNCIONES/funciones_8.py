#Ejercicio8. Definir una funcion que muestre en binario un número entre 0 y 255.

#http://recursostic.educacion.es/secundaria/edad/4esotecnologia/quincena5/imagenes5/pasar_decimal_binario.gif

def decimal_a_binario(n) :
  if n > 0 and n < 255 :
    sum = ''
    while n >= 1:
      r = n % 2
      sum =  str(r) + sum
      n = n//2
    print('el numero en binario es : '+ str(sum))

n = int(input('ingrese un numero: ')) 
