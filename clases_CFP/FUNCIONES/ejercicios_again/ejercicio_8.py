# Ejercicio 8 
# Definir una funcion que muestre en binario un número entre 0 y 255.

def binario(n):
    c = ''
    while n > 0:
        bit = n % 2
        c = str(bit) + c
        n //= 2
    print(c)

binario(9)        

def decimal_a_binario(n) :
  if n > 0 and n < 255 :
    sum=''
    while n >= 1:
      r = n % 2
      sum =  str(r) + sum
      n = n//2
    print('el numero en binario es : '+ str(sum))
n = int(input('ingrese un numero: ')) 
decimal_a_binario(n)