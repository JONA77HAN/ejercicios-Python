#Ejercicio8. Definir una funcion que muestre en binario un número entre 0 y 255.

#http://recursostic.educacion.es/secundaria/edad/4esotecnologia/quincena5/imagenes5/pasar_decimal_binario.gif

def mostrar_en_binario(numero):
    if 0 <= numero <= 255:
        if numero == 0:
            print("El número 0 en binario es: 0")
        else:
            binario = ""
            while numero > 0:
                bit = numero % 2
                binario = str(bit) + binario
                numero //= 2
            print(f"{numero} en binario es: {binario}")
    else:
        print("El número está fuera del rango (0-255)")

# Ejemplos de uso:
mostrar_en_binario(42)
mostrar_en_binario(128)
mostrar_en_binario(255)
mostrar_en_binario(0)
mostrar_en_binario(300)





