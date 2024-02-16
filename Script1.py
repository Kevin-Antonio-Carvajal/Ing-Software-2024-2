def tenis():
    player1 = input("Nombre Jugador 1: ")
    print("Registrado")
    player2 = input("Nombre Jugador 2: ")
    print("Registrado\n")
    sets = [0, 0]
    juegos = [0, 0]
    puntos = [0, 0]
    saque = 0  # 0 para player1, 1 para player2

    def pointsStr(point):
        """
        Transforma el número de puntos en su representación textual.
        0, 1, y 2 puntos se convierten a "0", "15", y "30", respectivamente. 
        3 puntos se representan como "40", y cualquier valor por encima indica ("Advantage").
        """
        if point < 3:
            return ["0", "15", "30"][point]
        elif point == 3:
            return "40"
        else:
            return "Advantage"

    def imprimeMarcador():
        """
        Este método ofrece una vista del progreso del partido, indicando quién está sirviendo,
        junto con la puntuación actual en términos de tenis (0, 15, 30...) y el conteo de sets y juegos.
        """
        jugador1_puntos, jugador2_puntos = puntos
        serving = player1 if saque == 0 else player2
        if jugador1_puntos >= 3 and jugador2_puntos >= 3:
            if jugador1_puntos == jugador2_puntos:
                puntuacion = "40-40 (Deuce)"
            elif jugador1_puntos > jugador2_puntos:
                puntuacion = f"Adv.{player1}-40"
            else:
                puntuacion = f"40-Adv.{player2}"
        else:
            puntuacion = f"{pointsStr(jugador1_puntos)}-{pointsStr(jugador2_puntos)}"
        print(f"Saque: {serving} | {player1} vs {player2} - Sets: {sets[0]}-{sets[1]}, Juegos: {juegos[0]}-{juegos[1]}, Puntos: {puntuacion}")

    def verificarGanador():
        """
        este metodo verifica si hay un ganador del juego actual y actualiza el marcador.
        si es necesario cambiar de cancha se realiza una impresión adicional.
        """
        nonlocal saque
        if max(puntos) >= 4 and abs(puntos[0] - puntos[1]) >= 2:
            ganadorJuego = player1 if puntos[0] > puntos[1] else player2
            print(f"Juego para {ganadorJuego}")
            if ganadorJuego == player1:
                juegos[0] += 1
            else:
                juegos[1] += 1
            puntos[0], puntos[1] = 0, 0
            verificaSet()
            saque = 1 - saque
            if sum(juegos) % 2 != 0:
                print("Cambio de cancha.")

    def verificaSet():
        """
        Este proceso incluye la reinicialización de los marcadores de juego para el nuevo set y, si es aplicable, 
        la declaración del ganador del partido basándose en el total de sets ganados.
        """
        if max(juegos) >= 6 and abs(juegos[0] - juegos[1]) >= 2:
            set_winner = player1 if juegos[0] > juegos[1] else player2
            print(f"Set para {set_winner}")
            if set_winner == player1:
                sets[0] += 1
            else:
                sets[1] += 1
            juegos[0], juegos[1] = 0, 0
            if max(sets) == 2:
                print(f"{set_winner} gana el partido {sets[0]}-{sets[1]} sets.")
                exit()

    # Bucle principal que se ejecuta hasta que se interrumpe el programa. Solicita quién gana cada punto y actualiza el marcador.
    while True:
        imprimeMarcador()
        try: #aqui incluimos al menos una estructura de control try-except
            entrada = input("Quién gana el punto? (Ingresa el nombre del jugador o 1/2): ").strip()
            if entrada.lower() not in [player1.lower(), player2.lower(), "1", "2"]:
                raise ValueError("\nEntrada inválida. Debe ser el nombre del jugador o 1/2.\n")
            if entrada.lower() == player1.lower() or entrada == "1":
                puntos[0] += 1
            else:
                puntos[1] += 1
            verificarGanador()
        except ValueError as e:
            print(e)
            continue  # Permite al usuario reintentar después de un error

tenis()
