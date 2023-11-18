def en_binario(n):
    binario = ''
    while n > 0:
        bit = n % 2
        binario = str(bit) + binario
        n = n // 2
    print ('El numero en binario es -----> ' + str(binario) ) 


en_binario(250)

