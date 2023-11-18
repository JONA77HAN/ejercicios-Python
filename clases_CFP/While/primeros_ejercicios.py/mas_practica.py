# Ejercicio10. 
# Pedir un número de 0 a 99 y mostrarlo escrito. 
# Por ejemplo, para 56 mostrar: cincuenta y seis.

# Resuelve: Carranza

numero = int(input('Ingrese un número de 0 a 99: '))

if numero < 16:
    if numero == 0:
        numeroEscrito = 'cero'
    if numero == 1:
        numeroEscrito = 'uno'
    if numero == 2:
        numeroEscrito = 'dos'
    if numero == 3:
        numeroEscrito = 'tres'
    if numero == 4:
        numeroEscrito = 'cuatro'
    if numero == 5:
        numeroEscrito = 'cinco'
    if numero == 6:
        numeroEscrito = 'seis'
    if numero == 7:
        numeroEscrito = 'siete'
    if numero == 8:
        numeroEscrito = 'ocho'
    if numero == 9:
        numeroEscrito = 'nueve'
    if numero == 10:
        numeroEscrito = 'diez'
    if numero == 11:
        numeroEscrito = 'once'
    if numero == 12:
        numeroEscrito = 'doce'
    if numero == 13:
        numeroEscrito = 'trece'
    if numero == 14:
        numeroEscrito = 'catorce'
    if numero == 15:
        numeroEscrito = 'quince'
else:
    decena = numero // 10
    unidad = numero % 10 
    if decena == 2:
        decenaTexto = 'veinte'
    if decena == 3:
        decenaTexto = 'treinta'
    if decena == 4:
        decenaTexto = 'cuarenta'
    if decena == 5:
        decenaTexto = 'cincuenta'
    if decena == 6:
        decenaTexto = 'sesenta'
    if decena == 7:
        decenaTexto = 'setenta'
    if decena == 8:
        decenaTexto = 'ochenta'
    if decena == 9:
        decenaTexto = 'noventa'

    if unidad == 0:
        numeroEscrito = decenaTexto
    else:
        if unidad == 1:
            unidadTexto = 'uno'
        if unidad == 2:
            unidadTexto = 'dos'
        if unidad == 3:
            unidadTexto = 'tres'
        if unidad == 4:
            unidadTexto = 'cuatro'
        if unidad == 5:
            unidadTexto = 'cinco'
        if unidad == 6:
            unidadTexto = 'seis'
        if unidad == 7:
            unidadTexto = 'siete'
        if unidad == 8:
            unidadTexto = 'ocho'
        if unidad == 9:
            unidadTexto = 'nueve'
        numeroEscrito = decenaTexto + ' y ' + unidadTexto
print('El número escrito es:', numeroEscrito)