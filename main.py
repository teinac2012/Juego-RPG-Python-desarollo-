def inicio():

    #Propiedades del jugador
    nombre = ""
    vida = 100
    ataque = 15
    energia = 100
    curacion = 10
    costeCuracion = 30
    xp = 0

    #Propiedades enemigo 1
    nombreEnemigo1 = "Troll"
    vidaEnemigo1 = 35
    ataqueEnemigo1 = 6

    #Comienzo del juego
    print("Despierta....Despierta...")
    import time
    time.sleep(2)
    nombre = input("¿Cómo te llamas? --Escribe tu nombre-- ->")
    print("Encantado de conocerte, " + nombre)
    import time
    time.sleep(2)
    print("Estas son tus estadisticas: ")
    import time
    time.sleep(2)
    print("Tu vida: " + str(vida))
    import time
    time.sleep(2)
    print("Tu energia: " + str(energia))
    import time
    time.sleep(2)
    print("Tu ataque: " + str(ataque))
    import time
    time.sleep(2)
    print("Cuanto restauras de vida usando tu curación: " + str(curacion))
    import time
    time.sleep(2)
    print("Cuanta energía gasta usar tu curación: " + str(curacion))
    import time
    time.sleep(3)
    print("--Acabas de entrar a Endzort--")
    import time
    time.sleep(3)

    #Presentación enemigouno
    print("Ha aparecido un " + nombreEnemigo1 + (":"))
    import time
    time.sleep(1)
    #Comenzamos combate1
    print("Tu vida: " + str(vida))
    import time
    time.sleep(1)
    print("Vida del enemigo: " + str(vidaEnemigo1))
    import time
    time.sleep(1)
    print("Tu energia: " + str(energia))
    import time
    time.sleep(1)

    while vida > 0 and vidaEnemigo1 > 0:
        import time
        time.sleep(1)

        respuesta = ""
        respuesta = input("¿Qué deseas hacer? a-atacar b-curar ->")

        if respuesta == "a":
            print("¡Has decidido atacar!")
            vidaEnemigo1 -= ataque

        elif respuesta == "b" and energia <= costeCuracion:
            print("No tienes sufieciente energia para curarte, has atacado")
            vidaEnemigo1 -= ataque
            import time
            time.sleep(1)

        elif respuesta == "b" and energia >= costeCuracion:
            print("¡Has decidido curarte!")
            energia -= costeCuracion
            vida += curacion

        else:
            print("Respuesta incorrecta o no reconocida, has atacado")
            vidaEnemigo1 -= ataque
            import time
            time.sleep(2)

        import time
        time.sleep(1)

        print("El " + nombreEnemigo1 + " te ataca y te quita " +
              str(ataqueEnemigo1) + " de vida")
        vida -= ataqueEnemigo1

        import time
        time.sleep(1)

        print("Tu vida: " + str(vida))
        import time
        time.sleep(1)
        print("Vida del enemigo:" + str(vidaEnemigo1))
        import time
        time.sleep(1)
        print("Tu energia: " + str(energia))

    if vida < 0:
        muerte()
    print("¡Has ganado el combate!")

    #Enemigo2
    vidaEnemigo2 = 50
    ataqueEnemigo2 = 1400
    nombreEnemigo2 = "Goblin"

    #objetos enemigo1 finalizar combate
    import time
    time.sleep(2)
    print("¡El enemigo soltó un casco!¿Qué quieres hacer con el?")
    respuesta = ""
    import time
    time.sleep(2)
    respuesta = input("a-ponerte el casco +6ps +4 ataque  b-tirarlo ->")

    if respuesta == "a":
        print("¡Has decidido ponertelo (+6ps +2 ataque)!")
        vida += 6
        ataque += 4
        import time
        time.sleep(1)
        print("Tu vida: " + str(vida))
        import time
        time.sleep(1)
        print("Tu ataque: " + str(ataque))

    elif respuesta == "b":
        print("¡Has decidido tirarlo!")
        import time
        time.sleep(1)
        print("Tu vida: " + str(vida))
        import time
        time.sleep(1)
        print("Tu ataque: " + str(ataque))

    else:
        print("Respuesta incorrecta o no reconocida, lo has soltado")
        import time
        time.sleep(1)
        print("Tu vida: " + str(vida))
        import time
        time.sleep(1)
        print("Tu ataque: " + str(ataque))

    import time
    time.sleep(2)

    #Diálogo1
    print("Se te acerca un aldeano, qué haces?")
    respuesta = ""
    import time
    time.sleep(1)
    respuesta = input("a-irte  b-hablar con el ->")
    import time
    time.sleep(1)
    if respuesta == "a":
        import time
        time.sleep(1)
        print("--Has decidido irte--")

    elif respuesta == "b":

        vida += 30

        print("Hola " + nombre + (
            " bienvenid@ a esta isla, ten mucho cuidado con las criaturas que andan por la orrilla, son...... peligrosas"
        ))
        import time
        time.sleep(3)
        print("Siempre que quieras curarte ven aqui y te curaré")
        import time
        time.sleep(2)
        print("--El aldeano te ha curado 30 de  vida y 30 de tu energia--")

        print("Tu vida: " + str(vida))
        import time
        time.sleep2
        print("Tu maná: " + str(energia))
        print("-------------------------------")
    else:
        print("Respuesta incorrecta o no reconocida , te has ido")

    while vida > 0 and vidaEnemigo2 > 0:
        #Presentación enemigouno
        print("Ha aparecido un " + nombreEnemigo2 + (":"))
        import time
        time.sleep(1)
        #Comenzamos combate1
        print("Tu vida: " + str(vida))
        import time
        time.sleep(1)
        print("Vida del enemigo: " + str(vidaEnemigo2))
        import time
        time.sleep(1)
        print("Tu energia: " + str(energia))
        import time
        time.sleep(1)
        import time
        time.sleep(1)

        respuesta = ""
        respuesta = input("¿Qué deseas hacer? a-atacar b-curar ->")

        if respuesta == "a":
            print("¡Has decidido atacar!")
            vidaEnemigo2 -= ataque

        elif respuesta == "b" and energia <= costeCuracion:
            print("No tienes sufieciente energia para curarte, has atacado")
            vidaEnemigo2 -= ataque
            import time
            time.sleep(1)

        elif respuesta == "b" and energia >= costeCuracion:
            print("¡Has decidido curarte!")
            energia -= costeCuracion
            vida += curacion

        else:
            print("Respuesta incorrecta o no reconocida, has atacado")
            vidaEnemigo2 -= ataque
            import time
            time.sleep(2)

        import time
        time.sleep(1)

        print("El " + nombreEnemigo2 + " te ataca y te quita " +
              str(ataqueEnemigo2) + " de vida")
        vida -= ataqueEnemigo2

        import time
        time.sleep(1)

        print("Tu vida: " + str(vida))
        import time
        time.sleep(1)
        print("Vida del enemigo:" + str(vidaEnemigo2))
        import time
        time.sleep(1)
        print("Tu energia: " + str(energia))

    if vida < 0:
        muerte()
    print("¡Has ganado el combate!")

    import time
    time.sleep(1)
    print("¡Has ganado el combate! +65 de xp")
    xp += 65
    import time
    time.sleep(2)
    print("Tu xp: " + str(xp) + " (35 de xp restante para el nivel 2)")


def muerte():
    respuesta = ""
    import time
    time.sleep(1)
    respuesta = input(
        "¡Has muerto! ¿Qué deseas hacer? a-empezar de nuevo b-salir ->")

    if respuesta == "a":
        inicio()
    elif respuesta == "b":
        print("¡Hasta luego!")
        import time
        time.sleep(999)
        import time
        time.sleep(9999)
        import time
        time.sleep(9999)
        import time
        time.sleep(9999)
        import time
        time.sleep(9999)
        import time
        time.sleep(9999)
        import time
        time.sleep(9999)
        import time
        time.sleep(999)
        import time
        time.sleep(999)
        import time
        time.sleep(999)
        import time
        time.sleep(999)
        import time
        time.sleep(999)
        import time
        time.sleep(999)
        import time
        time.sleep(999)
        import time
        time.sleep(999)
        import time
        time.sleep(999)
        import time
        time.sleep(999)
        import time
        time.sleep(999)
        import time
        time.sleep(999)
        import time
        time.sleep(999)

        print("Chao")
    else:
        print("¡Hasta luego!")
        import time
        time.sleep(9999)
        import time
        time.sleep(9999)
        import time
        time.sleep(9999)
        import time
        time.sleep(9999)
        import time
        time.sleep(9999)
        import time
        time.sleep(9999)
        import time
        time.sleep(9999)
        import time
        time.sleep(9999)
        import time
        time.sleep(9999)
        import time
        time.sleep(999)
        import time
        time.sleep(999)
        import time
        time.sleep(999)
        import time
        time.sleep(999)
        import time
        time.sleep(999)
        import time
        time.sleep(999)
        import time
        time.sleep(999)
        import time
        time.sleep(999)
        import time
        time.sleep(999)

        print("Chao")


inicio()

