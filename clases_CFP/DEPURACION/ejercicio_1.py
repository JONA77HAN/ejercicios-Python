#EjercicioDepuracion1. Semaforo de 3 tiempos.
"""
calleRivadavia = {'eo': 'rojo'}
calleJujuy = {'ns': 'verde'}
Estas 2 variables son para la intersección de Rivadavia y Jujuy. Para empezar necesitamos una
función cambiarLuces(), que tomará una intersección y cambiará las luces. Y para probar las
aserciones que acabamos de ver pondremos en el código algo que no queremos que ocurra
nunca.
Para este ejercicio pueden utilizar la función time.sleep(t) donde t es el número de segundos
que queremos detener el programa. Tendrán que importar el módulo time para poder usarla.
"""
#https://upload.wikimedia.org/wikipedia/commons/7/7b/Traffic_lights_3_states.svg
import time
def limpiarPantalla():
	print("\033c", end="")

def cambiarLuces(interseccion):

		for semaforo, color in interseccion.items():
			if color=='rojo':
				print(f'{semaforo} 🔴⚫⚫')
			else:
				print(f'{semaforo} ⚫⚫🟢')

		time.sleep(5)
		limpiarPantalla()

		for semaforo1,color in interseccion.items():
			print(f'{semaforo1} ⚫🟡⚫')
			for semaforo2, color in interseccion.items():
				if semaforo1 != semaforo2:
					if color=='rojo':
						print(f'{semaforo2} 🔴⚫⚫')
					else:
						print(f'{semaforo2} ⚫⚫🟢')
			limpiarPantalla()
			time.sleep(2)
			break

		estadoActual = interseccion.copy()

		interseccion['eo'] = estadoActual['ns']
		interseccion['ns'] = estadoActual['eo']

		time.sleep(5)
		limpiarPantalla()
		for semaforo1,color in interseccion.items():
			if color=='rojo':
				print(f'{semaforo1} 🔴⚫⚫')
			else:
				print(f'{semaforo1} ⚫⚫🟢')
			for semaforo2, color in interseccion.items():
				if semaforo1 != semaforo2:
					print(f'{semaforo2} ⚫🟡⚫')

			limpiarPantalla()
			time.sleep(2)
			break

		for semaforo, color in interseccion.items():
			if color=='rojo':
				print(f'{semaforo} 🔴⚫⚫')
			else:
				print(f'{semaforo} ⚫⚫🟢')
		time.sleep(1)


calleRivadavia = {'eo': 'rojo'}
calleJujuy = {'ns': 'verde'}
while True:

	interseccion = {**calleRivadavia, **calleJujuy}
	cambiarLuces(interseccion)
	limpiarPantalla()
	cambiarLuces(interseccion)
	limpiarPantalla()
