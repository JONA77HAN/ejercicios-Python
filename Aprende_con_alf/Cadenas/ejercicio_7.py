# Ejercicio 7
# Escribir un programa que pregunte el correo electrónico del usuario
# en la consola y muestre por pantalla otro correo electrónico con 
# el mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es.

frase = input('ingrese la frase: ')
frase_corta = frase[frase.find('f'):] #la ultima parte, desde la 'f'
frase_corta = frase[:frase.find('f')] #la primer parte, hasta la 'f'
print(frase_corta)
