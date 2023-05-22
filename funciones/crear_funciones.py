#usamos def para decirle al programa q crearemos nuestra propia funcion, funcion simple
#def saludar():
#    print ('hola lucas, como estas?')

#ejecuatando una funcion simple
#saludar()

#crear una funcion q tenga parametros
def saludar (nombre,sexo):
    sexo = sexo.lower()
    if (sexo =='mujer'):
        adjetivo = 'reina'
    elif (sexo =='hombre'):
        adjetivo = 'titan'
    else:
        adjetivo = 'amor'

    print (f'hola {nombre}, mi {adjetivo} como andas?')

saludar ('camila', 'mujer')
saludar ('leon', 'hombre') 
saludar ('fran', 'no binario')   

print ('------------------------------------------')

#creando una funcion q nos retorne valores:
def crear_contraseña_random(num):
    chars = 'abcdefghij'
    num_entero = str (num)
    num = int(num_entero[0])
    c1 = num -2
    c2 = num 
    c3 = num -5
    contraseña = f'{chars[c1]}{chars[c2]}{chars[c3]}{num*2}'
    return contraseña, num #nos quedamos tmb con el valor de la tupla

#desempaquetando la funcion
password, primer_numero = crear_contraseña_random(987)

#mostrando los resultados obtenidos y los datos utilizados para obtenerlo
print (f'tu contraseña nueva es: {password}')
print (f'el numero utilizado para crearla fue: {primer_numero}')