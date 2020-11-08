def inicio2():
   from poderes import personajes
   import time
   
   respuesta = ""
   respuesta = input("ಠ_ಠ --Pulsa cualquier botón para empezar-- ಠ_ಠ  ")

   if respuesta == "a":
     time.sleep(1)
     inicio()
   elif respuesta == "a":
      time.sleep(1)
      inicio()
   else:
      inicio()
      time.sleep(1)

def inicio():

    #Propiedades del jugador
    nombre = ""
    vida = 100
    ataque = 15
    energia = 100
    curacion = 10
    costeCuracion = 30
    xp = 0
    nivel = 1

    #Propiedades enemigo 1
    nombreEnemigo1 = "Troll"
    vidaEnemigo1 = 35
    ataqueEnemigo1 = 6
    import time
    #Comienzo del juego
    print("Despierta....Despierta...")
    time.sleep(2)
    nombre = input("¿Cómo te llamas? --Escribe tu nombre-- ->")
    print("Encantado de conocerte, " + nombre)
    time.sleep(2)
    print("Estas son tus estadisticas: ")
    time.sleep(2)
    print("Tu vida: " + str(vida))
    time.sleep(2)
    print("Tu energia: " + str(energia))
    time.sleep(2)
    print("Tu ataque: " + str(ataque))
    time.sleep(2)
    print("Cuanto restauras de vida usando tu curación: " + str(curacion))
    time.sleep(2)
    print("Cuanta energía gasta usar tu curación: " + str(curacion))
    time.sleep(3)
    print("   ----Acabas de entrar a Endzort----")
    time.sleep(3)

    #Presentación enemigouno
    print("Ha aparecido un " + nombreEnemigo1 + (":"))
    time.sleep(1)
    #Comenzamos combate1
    print("Tu vida: " + str(vida))
    time.sleep(1)
    print("Vida del enemigo: " + str(vidaEnemigo1))
    time.sleep(1)
    print("Tu energia: " + str(energia))
    time.sleep(1)

    while vida > 0 and vidaEnemigo1 > 0:
        time.sleep(1)

        respuesta = ""
        respuesta = input("¿Qué deseas hacer? a-atacar b-curar ->")

        if respuesta == "a":
            print("¡Has decidido atacar!")
            vidaEnemigo1 -= ataque

        elif respuesta == "b" and energia <= costeCuracion:
            print("No tienes sufieciente energia para curarte, has atacado")
            vidaEnemigo1 -= ataque
            time.sleep(1)

        elif respuesta == "b" and energia >= costeCuracion:
            print("¡Has decidido curarte!")
            energia -= costeCuracion
            vida += curacion

        else:
            print("Respuesta incorrecta o no reconocida, has atacado")
            vidaEnemigo1 -= ataque
            time.sleep(2)

        time.sleep(1)

        print("El " + nombreEnemigo1 + " te ataca y te quita " +
              str(ataqueEnemigo1) + " de vida")
        vida -= ataqueEnemigo1

        time.sleep(1)

        print("Tu vida: " + str(vida))
        time.sleep(1)
        print("Vida del enemigo:" + str(vidaEnemigo1))
        time.sleep(1)
        print("Tu energia: " + str(energia))

    if vida < 0:
        muerte()
    print("¡Has ganado el combate!")

    #Enemigo2
    vidaEnemigo2 = 50
    ataqueEnemigo2 = 14
    nombreEnemigo2 = "Goblin"

    #objetos enemigo1 finalizar combate
    time.sleep(2)
    print("¡El enemigo soltó un casco!¿Qué quieres hacer con el?")
    respuesta = ""
    time.sleep(2)
    respuesta = input("a-ponerte el casco +6ps +4 ataque  b-tirarlo ->")

    if respuesta == "a":
        print("¡Has decidido ponertelo (+6ps +2 ataque)!")
        vida += 6
        ataque += 4
        time.sleep(1)
        print("Tu vida: " + str(vida))
        time.sleep(1)
        print("Tu ataque: " + str(ataque))

    elif respuesta == "b":
        print("¡Has decidido tirarlo!")
        time.sleep(1)
        print("Tu vida: " + str(vida))
        time.sleep(1)
        print("Tu ataque: " + str(ataque))

    else:
        print("Respuesta incorrecta o no reconocida, lo has soltado")
        time.sleep(1)
        print("Tu vida: " + str(vida))
        time.sleep(1)
        print("Tu ataque: " + str(ataque))

    time.sleep(2)

    #Diálogo1
    print("Se te acerca un aldeano, qué haces?")
    respuesta = ""
    time.sleep(1)
    respuesta = input("a-irte  b-hablar con el ->")
    time.sleep(1)
    if respuesta == "a":
        time.sleep(1)
        print("--Has decidido irte--")
        time.sleep(1)

    elif respuesta == "b":

        vida += 30

        print("Hola " + nombre + (
            " bienvenid@ a esta isla, ten mucho cuidado con las criaturas que andan por la orrilla, son peligrosas"
        ))
        time.sleep(4)
        print("Siempre que quieras curarte ven aqui y te curaré")
        time.sleep(2)
        print("--El aldeano te ha curado 30 de  vida y 30 de tu energia--")

        print("Tu vida: " + str(vida))
        time.sleep(2)
        print("Tu maná: " + str(energia))
        time.sleep(1)
        print("-------------------------------")
    else:
        print("Respuesta incorrecta o no reconocida , te has ido")
        time.sleep(1)
        print("-------------------------------")
    #Presentación enemigo2
    print("Ha aparecido un " + nombreEnemigo2 + (":"))
    time.sleep(1)
    print("Tu vida: " + str(vida))
    time.sleep(1)
    print("Vida del enemigo: " + str(vidaEnemigo2))
    time.sleep(1)
    print("Tu energia: " + str(energia))
    time.sleep(1)
    while vida > 0 and vidaEnemigo2 > 0:

        #Comenzamos combate2

        time.sleep(1)

        respuesta = ""
        respuesta = input("¿Qué deseas hacer? a-atacar b-curar ->")

        if respuesta == "a":
            print("¡Has decidido atacar!")
            vidaEnemigo2 -= ataque

        elif respuesta == "b" and energia <= costeCuracion:
            print("No tienes sufieciente energia para curarte, has atacado")
            vidaEnemigo2 -= ataque
            time.sleep(1)

        elif respuesta == "b" and energia >= costeCuracion:
            print("¡Has decidido curarte!")
            energia -= costeCuracion
            vida += curacion

        else:
            print("Respuesta incorrecta o no reconocida, has atacado")
            vidaEnemigo2 -= ataque
            time.sleep(2)

        time.sleep(1)

        print("El " + nombreEnemigo2 + " te ataca y te quita " +
              str(ataqueEnemigo2) + " de vida")
        vida -= ataqueEnemigo2

        time.sleep(1)

        print("Tu vida: " + str(vida))
        time.sleep(1)
        print("Vida del enemigo:" + str(vidaEnemigo2))
        time.sleep(1)
        print("Tu energia: " + str(energia))

    if vida < 0:
        muerte()

    time.sleep(1)
    print("¡Has ganado el combate! +65 de xp")
    xp += 150
    time.sleep(2)
    if xp >= 100:
      nivel += 1
      print("!Has subido al nivel "+str(nivel)+(" !!"))
      time.sleep(2)
      respuesta = ""
      respuesta = input("¿Qué deseas hacer? a-Aprender/mejorar habilidad b-Guardarte la xp ->")
      time.sleep(1)
      if respuesta == "a":
        print("Tienes "+str(xp)(" de experiencia"))
        if xp >= 120:
          time.sleep(1)
          respuesta = ""
          respuesta = input("¿Qué deseas hacer? a-ver habilidades b-descartar ->")
          if respuesta =="a":
            time.sleep(1)
            print("Habilidades que puedes mejorar o aprender:")
            if xp >= 100 and xp <= 150:
              time.sleep(1)
              respuesta = input("a-mejorar curación +6 (-100 xp) b-mejorar ataque +8(-100 xp) ->")
              if respuesta =="a":
                ataque += 8
                xp -= 2
                time.sleep(1)
                print("+8 de ataque (-100 de xp)")
              elif respuesta =="b":
                time.sleep(1)
                print("+6 de curación (-100 de xp)")
                xp -= 2
                curacion += 6

      elif respuesta == "b":
            print("Has decidido guardate la xp")



    elif xp <= 100: print("Tu xp: " + str(xp) + " (35 de xp restante para el nivel 2)")
   


def muerte():
    import time
    respuesta = ""
    time.sleep(1)
    respuesta = input(
        "¡Has muerto! ¿Qué deseas hacer? a-empezar de nuevo b-salir ->")

    if respuesta == "a":
        inicio()
    elif respuesta == "b":
        print("¡Hasta luego!")
        time.sleep(999)
        time.sleep(9999)
        time.sleep(9999)
        time.sleep(9999)
        time.sleep(9999)
        time.sleep(9999)
        time.sleep(9999)
        time.sleep(999)
        time.sleep(999)
        time.sleep(999)
        time.sleep(999)
        time.sleep(999)
        time.sleep(999)
        time.sleep(999)
        time.sleep(999)
        time.sleep(999)
        time.sleep(999)
        time.sleep(999)
        time.sleep(999)
        time.sleep(999)

        print("Chao")
    else:
        print("¡Hasta luego!")
        time.sleep(9999)
        time.sleep(9999)
        time.sleep(9999)
        time.sleep(9999)
        time.sleep(9999)
        time.sleep(9999)
        time.sleep(9999)
        time.sleep(9999)
        time.sleep(9999)
        time.sleep(999)
        time.sleep(999)
        time.sleep(999)
        time.sleep(999)
        time.sleep(999)
        time.sleep(999)
        time.sleep(999)
        time.sleep(999)
        time.sleep(999)

        print("Chao")


inicio2()
