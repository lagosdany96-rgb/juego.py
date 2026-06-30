seguir = "S"

while seguir == "S" or seguir == "s":

    jugador = input("\nIngresa tu nombre para iniciar la partida: ")

    jugar(jugador)

    seguir = input("\n¿Deseas jugar nuevamente? (S/N): ")