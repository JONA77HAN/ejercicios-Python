saludo = 'hola universo'
print(saludo[0:4])
print('hola' in 'hola mundo')
print(saludo.upper())
print('-'*50)
print('Cómo estás?')
meSiento = input()
if meSiento.lower() == 'bien':
 print('Yo me siento genial también!')
else:
 print('Espero que el resto de tu día mejore.')
 print('-'*50)
 # Los metodos islower() y isupper() devuelve True o False segun sea el caso
 comoEstas = input('como estas?')
 if comoEstas.lower() == 'bien':
  print('que bueno q estes bien')
 else:
  print('q te paso?')
