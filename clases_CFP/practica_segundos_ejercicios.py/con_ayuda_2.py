numero = int(input("Ingrese un número de 0 a 99: "))

if numero < 16:
    if numero == 0:
        numero_escrito = "cero"
    if numero == 1:
        numero_escrito = "uno"
    if numero == 2:
        numero_escrito = "dos"
    if numero == 3:
        numero_escrito = "tres"
    if numero == 4:
        numero_escrito = "cuatro"
    if numero == 5:
        numero_escrito = "cinco"
    if numero == 6:
        numero_escrito = "seis"
    if numero == 7:
        numero_escrito = "siete"
    if numero == 8:
        numero_escrito = "ocho"
    if numero == 9:
        numero_escrito = "nueve"
    if numero == 10:
        numero_escrito = "diez"
    if numero == 11:
        numero_escrito = "once"
    if numero == 12:
        numero_escrito = "doce"
    if numero == 13:
        numero_escrito = "trece"
    if numero == 14:
        numero_escrito = "catorce"
    if numero == 15:
        numero_escrito = "quince"
else:
    decena = numero // 10
    unidad = numero % 10

    if decena == 2:
        decenaTexto = "veinte"
    if decena == 3:
        decenaTexto = "treinta"
    if decena == 4:
        decenaTexto = "cuarenta"
    if decena == 5:
        decenaTexto = "cincuenta"
    if decena == 6:
        decenaTexto = "sesenta"
    if decena == 7:
        decenaTexto = "setenta"
    if decena == 8:
        decenaTexto = "ochenta"
    if decena == 9:
        decenaTexto = "noventa"

    if unidad == 0:
        numero_escrito = decenaTexto
    else:
        unidadTexto = ""
        if unidad == 1:
            unidadTexto = "uno"
        if unidad == 2:
            unidadTexto = "dos"
        if unidad == 3:
            unidadTexto = "tres"
        if unidad == 4:
            unidadTexto = "cuatro"
        if unidad == 5:
            unidadTexto = "cinco"
        if unidad == 6:
            unidadTexto = "seis"
        if unidad == 7:
            unidadTexto = "siete"
        if unidad == 8:
            unidadTexto = "ocho"
        if unidad == 9:
            unidadTexto = "nueve"

        numero_escrito = decenaTexto + ' y ' + unidadTexto

print("El número escrito es:", numero_escrito)
