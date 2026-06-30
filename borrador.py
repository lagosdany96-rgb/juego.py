import random

# -------- FUNCIONES --------

def guardar_resultado(nombre, puntaje):
    """Guarda el resultado del jugador en un archivo"""
    archivo = open("resultados.txt", "a")
    archivo.write(nombre + ": " + str(puntaje) + "\n")
    archivo.close()


def mostrar_resultados():
    """Muestra los resultados guardados"""
    archivo = open("resultados.txt", "r")
    print("\n--- Resultados anteriores ---")
    for linea in archivo:
        print(linea.strip())
    archivo.close()


def jugar(nombre):
    """Juego de adivinanza"""

    largo = len(nombre)

    # Lista de posibles números secretos
    posibles = list(range(1, largo + 1))

    # Número secreto aleatorio entre 1 y el largo del nombre
    numero_secreto = random.randint(1, largo)

    historial = []
    puntaje = 0
    adivino = False

    print("\n🔍 El número secreto estará entre 1 y", largo,
          "porque tu nombre tiene", largo, "letras 👽")
    print("\nTienes solo 3 intentos. ¡Buena suerte! 😎")

    # -------- CICLO FOR --------
    for intentos in range(1, 4):

        if adivino == False:

            intento = int(input("Intento " + str(intentos) + ": "))
            historial.append(intento)

            # -------- CONDICIONALES --------
            if intento == numero_secreto:
                print("¡Correcto! 🎉")
                puntaje = 4 - intentos
                adivino = True

            elif intento < numero_secreto:
                print("El número secreto es mayor.")

            else:
                print("El número secreto es menor.")

    # Si no adivinó
    if adivino == False:
        print("\n😢 No lograste adivinar.")
        print("El número secreto era:", numero_secreto)

    # -------- SALIDAS --------
    print("\nJuego terminado.")
    print("Puntaje:", puntaje)
    print("Historial de intentos:", historial)

    guardar_resultado(nombre, puntaje)


# -------- PROGRAMA PRINCIPAL --------

print("🎉 Bienvenidos a la Ruleta Sherlock Numbers 🎉")

seguir = "S"

while seguir == "S" or seguir == "s":

    jugador = input("\nIngresa tu nombre para iniciar la partida: ")

    jugar(jugador)

    seguir = input("\n¿Deseas jugar nuevamente? (S/N): ")

print("\nGracias por jugar. 👋")

mostrar_resultados()