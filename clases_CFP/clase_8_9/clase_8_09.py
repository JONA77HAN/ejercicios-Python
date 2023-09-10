#Ejercicio13. Pedir 10 sueldos. 
# Mostrar su suma y cuantos hay mayores de $1000.  
# Y decir cual fue el sueldo mas alto


from random import randint 
num = 0
sum = 0
mayor_a_mil = 0
sueldo_max = -1000  

for i in range (10) :
  num = randint (100,10000)
  sum = sum + num
print ('La suma de todos los sueldos es: \n' + str(sum) +' ' + 'pesos')

if num > 1000 :
  mayor_a_mil=mayor_a_mil + 1
print ('Hay'+' '+(str(mayor_a_mil)) + str(mayor_a_mil) +'' + ' '+'sueldos mayores a 1000 pesos')  

if num > sueldo_max :
  sueldo_max = num
  print ('El maximo sueldo es: \n' + ' '+str(sueldo_max)+' '+'pesos')