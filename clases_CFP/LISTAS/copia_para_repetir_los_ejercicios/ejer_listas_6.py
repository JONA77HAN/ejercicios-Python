from random import randint
lista = []
orden = ''
for i in range(5):
    num = int(input('ingrese un numero: ')) #randint(0, 3)  
    lista.append(num)
print(lista)
for i in range(len(lista) - 1):
    if lista[i] > lista[i + 1]:
        orden = 'decreciente'
    elif lista[i] < lista[i + 1]:
        orden = 'creciente'
    else:
        orden = 'desordenada'
        
if orden == 'creciente':
    print('creciente')
elif orden == 'decreciente':
    print('decreciente')
else:
    print('desordenada')        

