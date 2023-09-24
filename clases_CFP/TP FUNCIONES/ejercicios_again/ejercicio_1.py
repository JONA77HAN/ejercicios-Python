# Funciones.Ejercicio1. 
# Definir una función:
# A la que se le pase como parámetro un número N y muestre por pantalla N veces 
# El mensaje: Módulo ejecutándose”.

def mostrar_msj(n):
    for i in range(n):
        print('Modulo Ejecutandose')

n = int(input('ingrese n: '))

mostrar_msj(n)