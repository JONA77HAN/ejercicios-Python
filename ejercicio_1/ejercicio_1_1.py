#duracion de cursos
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
dalto_curso = 1.5

#diferencia de duracion 
diferencia_con_min = 100 - dalto_curso / otros_cursos_min * 100
diferencia_con_max = 100 - dalto_curso * 1000 // otros_cursos_max / 10
diferencia_con_promedio = 100 - dalto_curso / otros_cursos_promedio * 100

#respuesta
print (f'el curso de Dalto dura {diferencia_con_min} % menos q el minimo de los otros cursos' )
print (f'el curso de Dalto dura {diferencia_con_max} % menos q el maximo de los otros cursos' )
print (f'el curso de Dalto dura {diferencia_con_promedio} % menos q el promedio de los otros cursos' )
print ('-----------------------------')
#mostrando diferencias si los cursos duraran 10 horas
print (f'ver 10 horas de este curso equivale a ver {otros_cursos_promedio *100 // dalto_curso / 10} horas de otros cursos ')
print (f'ver 10 horas de este curso equivale a ver {dalto_curso *100 //otros_cursos_promedio / 10} horas de otros cursos ')
print ('-----------------------------')