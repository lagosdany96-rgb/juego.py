import random

def guardar_resultado(nombre, puntaje):

    archivo = open("resultados.txt", "a")
    archivo.write(nombre + ": " + str(puntaje) + "\n")
    archivo.close()

def mostrar_resultados():

    archivo = open("resultados.txt", "r")
    print("\n--- Resultados anteriores ---")
    for linea in archivo:
        print(linea.strip())
    archivo.close()

def jugar(nombre):

    largo = len(nombre)
    numero_secreto = random.randint(1, largo)

    puntaje = 0
    adivino = False

    print("\n🔍 El número secreto estará entre 1 y", largo,
          "porque tu nombre tiene", largo, "letras.")
    print("Tienes solo 3 intentos. ¡Buena suerte! 😎")

    for intentos in range(1, 4):

        if adivino == False:

            intento = int(input("Intento " + str(intentos) + ": "))

            if intento == numero_secreto:
                print("¡Correcto! 🎉")

                if intentos == 1:
                    puntaje = 10
                elif intentos == 2:
                    puntaje = 7
                else:
                    puntaje = 4

                adivino = True
            elif intento < numero_secreto:
                print(" El numero secreto es mayor.")
            else:
                print("El numero secreto es menor.")

    if adivino == False:
        print("\n😢 No lograste adivinar.")
        print("El número secreto era:", numero_secreto)

    print("\n ¡Gracias por jugar,"+ nombre + "! Tu puntaje es:",puntaje)
    print("\n !Con esa suerte podrias jugarte un kino! 🛳️  🛟  ✈️")

    guardar_resultado(nombre, puntaje)


print("🎉 ¡Bienvenidos a la Ruleta Sherlock Numbers! 🎉")
print("\n🫡 ¡En este juego debes adivinar un número secreto que se encontrará entre el número 1 y el largo de tu nombre!🥸")
print("Comencemos...🤖")

seguir = "S"

while seguir.upper() == "S":

    jugador = input("\nIngresa tu nombre para iniciar la partida: ")

    jugar(jugador)

    seguir = input("\n¿Deseas jugar nuevamente? (S/N): ")

print("\nGracias por jugar. 👋")

mostrar_resultados()