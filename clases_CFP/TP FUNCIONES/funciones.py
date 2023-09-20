def hola():
    print('Hola!')
    print('Hola!!!')
    print('Hola mundo!')

hola()

print('¿estas comodo?')
longitud = len('yasmin')
print (longitud)

def hola(nombre):
    print(f'Hola {nombre} como te fue en el cole?')

hola('Lucio')

def elegir(a, b, c):
    if a > b and a > c:
        print(f'el numero a es el mas alto')
    elif b > c and b > a:
        print(f'el numero mas alto es el b')
    else:
        print(f'c es el mas alto q ingresaste')

elegir(151,2,522)