# Ejercicio 10
# La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. 
# Los ingredientes para cada tipo de pizza aparecen a continuación.
# Ingredientes vegetarianos: Pimiento y tofu.
# Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.

# Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, 
# y en función de su respuesta le muestre un menú con los ingredientes disponibles 
# para que elija. Solo se puede eligir un ingrediente además de la mozzarella y el 
# tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la 
# pizza elegida es vegetariana o no y todos los ingredientes que lleva.

tipo = int(input('Elije un tipo de pizza:\n1) Vegetariana\n2)No Vegetariana \n --> '))
if tipo == 1:
    print('elegiste piza Vegetariana:')
    pimientoOtofu = input('La quieres con Pimiento o Tofu: ')
    print('tu pizza Vegetariana tendra: Muzzarella, tomate y ', end="")
    if pimientoOtofu.lower() == 'pimiento':
        print('pimiento')
    else:
        print('Tofu')
else: 
    print('elegiste piza No Vegetariana:')
    salmonOjamon = input('La quieres con Salmon o Jamon: ')
    print('tu pizza No Vegetariana tendra: Muzzarella, tomate y ', end="")
    if salmonOjamon.lower() == 'salmon':
        print('salmon')
    else:
        print('jamon')        
