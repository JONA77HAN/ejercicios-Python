#vamos por aca, por el apunte 2
while True:
  print('Ingresar edad:')
  edad = input()
  if edad.isdecimal():
    break
  print('Por favor ingrese un número para la edad.')
  
while True:
   print('Ingrese una contraseña (letras y números solamente):')
   password = input()
   if password.isalnum():
    break
   print('La contraseña solo puede tener letras y números')