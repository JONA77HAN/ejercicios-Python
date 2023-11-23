#Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros) 
#calcule el índice de masa corporal y lo almacene en una variable, 
#y muestre por pantalla la frase: 
#Tu índice de masa corporal es <imc> donde <imc> es el 
#índice de masa corporal calculado redondeado con dos decimales.
print('voy a calcular tu masa corporal')
peso = int(input('ingresa tu peso: \n'))
altura = int(input('ingresa tu altura: \n'))
masa_corporal = round(peso / altura, 2)
print(f'Tu indice de masa corporal es {masa_corporal}')