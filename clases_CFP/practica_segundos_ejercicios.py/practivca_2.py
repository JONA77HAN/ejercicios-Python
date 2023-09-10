# %s para los strings
# %d para los numeros enteros
# %f para los numeros flotantes

name = "John"
print("Hello, %s!" % name)

name = "John"
age = 23
print("%s is %d years old." % (name, age))

mama = 'Yas'
papa = 'Jhonny'
hijoMayor = 'Leon'

print('la madre se llama %s, y el nombre del padre es %s' % (mama, papa))
print('el nombre del hijo mayor es %s' % hijoMayor)

hijo = 'Lucio'
apellido = 'Carranza'
edad = 5
altura = 1.20

print('su nombre es %s %s, tiene %d años y una altura de %f'%(hijo, apellido, edad, altura))

instrumento = 5
oracion = f'su instrumento favorito es la {instrumento}'


print (f'su instrumento es {instrumento}')