# ==========================
# JUEGO: CAMINO AL CFT ESTATAL
# ==========================

etapas = [
    "Terminal de Buses de Viña del Mar",
    "Esquina calle Quilpué con Viana",
    "Tiendas RIPLEY (calle Sucre con Viana)",
    "Sucursal Caja Los Andes (calle Quinta con Viana)",
    "CFT Estatal de Valparaíso"
]

puntajes = []

# ==========================
# CARGAR PUNTAJES
# ==========================

def cargar_puntajes():
    try:
        archivo = open("puntajes.txt", "r")

        for linea in archivo:
            datos = linea.strip().split(",")
            nombre = datos[0]
            puntos = int(datos[1])
            puntajes.append([nombre, puntos])

        archivo.close()

    except:
        print("No existen puntajes guardados.")

# ==========================
# GUARDAR PUNTAJE
# ==========================

def guardar_puntaje(nombre, puntos):
    archivo = open("puntajes.txt", "a")
    archivo.write(nombre + "," + str(puntos) + "\n")
    archivo.close()

# ==========================
# MOSTRAR RANKING
# ==========================

def mostrar_ranking():
    print("\n===== RANKING DE JUGADORES =====")

    if len(puntajes) == 0:
        print("No hay puntajes registrados.")
    else:
        contador = 1

        for jugador in puntajes:
            print(contador, "-", jugador[0], "-", jugador[1], "puntos")
            contador += 1

# ==========================
# JUGAR
# ==========================

def jugar():
    nombre = input("\nIngrese su nombre: ")

    puntos = 0
    posicion = 0
    usadas = []

    print("\nBienvenido", nombre)
    print("Tu misión es llegar al CFT Estatal Región de Valparaíso.")

    while posicion < len(etapas) - 1:

        print("\n========================")
        print("Ubicación actual:", etapas[posicion])
        print("========================")

        usadas = []  # reinicia opciones en cada etapa

        if posicion == 0:
            opciones = [
                "Caminar por calle quilpué hacia calle Viana",
                "Ir al Mall Paseo Viña Centro",
                "Quedarte en el Terminal"
            ]

        elif posicion == 1:
            opciones = [
                "Seguir por calle Viana",
                "Ir al Mall Paseo Viña Centro",
                "Volver al Terminal"
            ]

        elif posicion == 2:
            opciones = [
                "Seguir avanzando por Viana",
                "Entrar a Ripley a ver tu nuevo Outfit",
                "Volver atrás"
            ]

        elif posicion == 3:
            opciones = [
                "Seguir recto por Viana",
                "Ir hacia la playa",
                "Ir a conocer la Quinta Vergara"
            ]

        else:
            opciones = [
                "Seguir hasta el CFT",
                "Ir al mall",
                "Volver atrás"
            ]

        print("\n¿Qué deseas hacer?")

        i = 1
        for op in opciones:
            print(str(i) + ".", op)
            i += 1

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            posicion += 1
            puntos += 10
            print("\nAvanzaste correctamente.")

        elif opcion == "2":
            puntos -= 5
            print("\nTe desviaste.")

        elif opcion == "3":
            puntos -= 10
            print("\nRetrocediste o te perdiste.")

        else:
            print("\nOpción inválida.")

        print("Puntaje actual:", puntos)

    print("\n=================================")
    print("¡FELICIDADES!")
    print("Llegaste al CFT Estatal Región de Valparaíso.")
    print("Puntaje final:", puntos)
    print("=================================")

    puntajes.append([nombre, puntos])
    guardar_puntaje(nombre, puntos)

# ==========================
# MENÚ PRINCIPAL
# ==========================

def menu():
    cargar_puntajes()

    salir = False

    while salir == False:

        print("\n========================")
        print(" CAMINO AL CFT ESTATAL ")
        print("========================")
        print("1. Jugar")
        print("2. Ver Ranking")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            jugar()

        elif opcion == "2":
            mostrar_ranking()

        elif opcion == "3":
            salir = True
            print("\nGracias por jugar.")

        else:
            print("\nOpción incorrecta.")

# ==========================
# INICIO
# ==========================

menu()