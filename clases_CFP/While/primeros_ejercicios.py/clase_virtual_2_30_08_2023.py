#Ejercicio13. Pedir dos fechas y mostrar el número de días que hay de diferencia. Suponiendo todos los meses de 30 días.
 
print("Ingrese el primer dia")
diaA = int(input())      
print("Ingrese el primer mes")
mesA = int(input())      
print("Ingrese el primer año")
añoA = int(input())      

print("Ingrese el segundo dia")
diaB = int(input())
print("Ingrese el segundo dia")
mesB = int(input()) 
print("Ingrese el segundo dia")
añoB= int(input()) 

#Comparacion de dias 

dif_dia = diaA - diaB
if dif_dia < 0 :
  dif_dia = dif_dia * (-1)
  
#comparacion de meses

dif_mes = mesA - mesB
if dif_mes < 0 :
  dif_mes = dif_mes * (-1)
  dif_mes = dif_mes * 30
  
#comparacion de años

dif_años = añoA - añoB
if dif_años < 0 :
  dif_años = dif_años * (-1)
  dif_años = dif_años * 365

dif_final = dif_dia + dif_mes + dif_años

print("Hay " + str(dif_final) + " " + "dias de diferencia")