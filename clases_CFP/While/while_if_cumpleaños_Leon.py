while True:
 nombre = input ('Escribe tu nombre: \n')
 print(f'Hola {nombre} como estás')
 estado_de_animo = input()

 if estado_de_animo == 'bien' or estado_de_animo == 'muy bien' or estado_de_animo == 'super bien ' or estado_de_animo == 'excelente' or estado_de_animo == 'de diez':
  print (f'que bueno q estes {estado_de_animo}, {nombre} ¿es verdad que hoy es tu cumpleaños?')
  cumpleaños_si_o_no = input()
 else:
  print(f'uh! ¿en serio? ¿por qué {estado_de_animo}?')
  motivos_mal = input()
  break

 if cumpleaños_si_o_no == 'si':
  print(f'FELIZ CUMPLEAÑOS {nombre} !!!!!')
  print(f'anda pensando tus deseos de cumpleaños {nombre}')
  print(f'estuviste viendo Minecraft hoy?')
  si_vio_minecraft = input()
  if si_vio_minecraft == 'si':
   print('que buen juego!')
 else:
  print ('Pero tu cumpleaños no es el 7 de Septiembre?')
  respuesta_nueva_sobre_cumpleaños = input()


