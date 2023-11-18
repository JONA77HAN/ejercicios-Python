#Ejercicio2. Escribir un programa que pueda agregar texto a un archivo y luego mostrarlo.

sonetoDir = './Soneto29.txt'
sonetoArc = open(sonetoDir,'a')
texto = input('Ingrese texto: ')
sonetoArc.write(texto)
sonetoArc.close()
sonetoArc = open(sonetoDir)
sonetoCont = sonetoArc.read()
sonetoArc.close()
print(sonetoCont)