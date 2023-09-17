from random import randint

# Función para obtener el valor de una carta
def valor_carta(carta):
    if carta in [1, 11, 12, 13]:
        return 10
    else:
        return carta

# Función para jugar la mano del croupier
def jugar_croupier():
    mano_croupier = []
    while sum(mano_croupier) <= 16:
        carta = randint(1, 13)
        mano_croupier.append(valor_carta(carta))
    return mano_croupier

# Función para jugar la mano del jugador
def jugar_jugador():
    mano_jugador = []
    while True:
        opcion = input("¿Quieres pedir una carta (p) o plantarte (pl)? ").lower()
        if opcion == 'p':
            carta = randint(1, 13)
            mano_jugador.append(valor_carta(carta))
            print("Tu mano:", mano_jugador)
            if sum(mano_jugador) > 21:
                print("Te pasaste de 21. Pierdes.")
                return mano_jugador
        elif opcion == 'pl':
            return mano_jugador

# Función para determinar el resultado
def determinar_resultado(mano_jugador, mano_croupier):
    puntaje_jugador = sum(mano_jugador)
    puntaje_croupier = sum(mano_croupier)
    
    if puntaje_jugador > 21:
        return "El croupier gana. Te pasaste de 21."
    elif puntaje_croupier > 21:
        return "¡Ganaste! El croupier se pasó de 21."
    elif puntaje_jugador > puntaje_croupier:
        return "¡Ganaste! Tu puntaje es mayor que el del croupier."
    elif puntaje_jugador < puntaje_croupier:
        return "El croupier gana. Su puntaje es mayor que el tuyo."
    else:
        return "Es un empate. Ambos tienen el mismo puntaje."

# Función principal del juego
def jugar_blackjack():
    print("¡Bienvenido a Blackjack!")
    
    # Iniciar la mano del croupier y el jugador
    mano_croupier = [randint(1, 13)]
    mano_jugador = [randint(1, 13), randint(1, 13)]
    
    print("Tu mano:", mano_jugador)
    
    # Jugar la mano del jugador
    mano_jugador = jugar_jugador()
    
    # Jugar la mano del croupier
    mano_croupier = jugar_croupier()
    
    # Determinar el resultado
    resultado = determinar_resultado(mano_jugador, mano_croupier)
    print("Mano del croupier:", mano_croupier)
    print(resultado)

# Ejecutar el juego
jugar_blackjack()
