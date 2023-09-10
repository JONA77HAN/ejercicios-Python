print('Ingrese el primer numero: ')
numeroA = int(input())

print('Ingrese el segundo numero: ')
numeroB = int(input())

print('Ingrese el tercer numero: ')
numeroC = int(input())

if numeroA < numeroB:
    if numeroA < numeroC:
        numeroMenor = numeroA
if numeroB < numeroA:
    if numeroB < numeroC:
        numeroMenor = numeroB
if numeroC < numeroA:
    if numeroC < numeroB:
        numeroMenor = numeroC

if numeroA > numeroB:
    if numeroA > numeroC:
        numeroMayor = numeroA
if numeroB > numeroA:
    if numeroB > numeroC:
        numeroMayor = numeroB
if numeroC > numeroA:
    if numeroC > numeroB:
        numeroMayor = numeroC

if numeroMenor < numeroA < numeroMayor:
    numeroDelMedio = numeroA


if numeroMenor < numeroB < numeroMayor:
    numeroDelMedio = numeroB


if numeroMenor < numeroC < numeroMayor:
    numeroDelMedio = numeroC

print('el orden de menor a mayor es: ' + str(numeroMenor) + ' ' + str(numeroDelMedio) + ' ' + str(numeroMayor))