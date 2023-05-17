lista = ["Jonathan Carranza", "Yasmin", True, 1.78]
#datos q adentro tienen otros datos

lista[0]= "Fernando"
#asi modifico un dato
print (lista)

tupla = ("Jonathan Carranza", "Yasmin", True, 1.78)
#las tuplas no pueden modificarse
#no olvidemos q en progr contamos desde 0, el primer elemento es el q esta en el indice 0

print (tupla[3])  

#creando un conjunto (set)

conjunto = {"Jonathan Carranza", "Yasmin", True, 1.78}
#no podemos modificar los elementos
#no podemos acceder por un indice
#no me permite repetir valores (no duplica datos)
#y son datos desordenados

print (conjunto)

diccionario = {
    'nombre' : "Leon Carranza",
    'edad': 7,
    'colegio': "Mercedes Pacheco",
    'dato duplicado': "Leon Carranza"
}
#podes usar el indice no con posc, si no con el nombre
#la estructura es key:value, se ultizan comas

print (diccionario['edad'])

lista_definitiva = {
    'mama': "yasmin",
    'papa': "johnny",
    'hermano_mayor': "Leon",
    'hermano_menor': "Lucio"
}

lista_definitiva['hermano_menor']= "Carranza"
lista_definitiva['mama']= "Daiana"

print (lista_definitiva['hermano_menor'])

#lista, tupla, conjunto, diccionario
colores = ['rojo', 'amarillo', 'verde','violeta']
condimentos = ('ajo', 'sal', 'romero')
conjuntos = {'amapola', 'lirio', 'lavanda'}

dic = {
    'nombre': "claudia",
    'apellido': "muñoz",
    'edad' : 50
}

print ()