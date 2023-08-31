numero = int(input("Ingrese un número de 0 a 99: "))

if numero < 16:
    # Números del 1 al 15
    numeros_hasta_15 = [
        "cero", "uno", "dos", "tres", "cuatro", "cinco", 
        "seis", "siete", "ocho", "nueve", "diez", 
        "once", "doce", "trece", "catorce", "quince"
    ]
    numero_escrito = numeros_hasta_15[numero]
else:
    decenas = ["", "diez", "veinte", "treinta", "cuarenta", "cincuenta", "sesenta", "setenta", "ochenta", "noventa"]
    unidades = ["", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve"]

    decena = numero // 10
    unidad = numero % 10

    decenaTexto = decenas[decena]
    unidadTexto = unidades[unidad]

    if unidad == 0:
        numero_escrito = decenaTexto
    else:
        numero_escrito = decenaTexto + ' y ' + unidadTexto

print("El número escrito es:", numero_escrito)
