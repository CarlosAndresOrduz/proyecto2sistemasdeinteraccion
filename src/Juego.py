from prueba import run

# Sección 1: Contexto Inicial y Configuración

def mostrar_contexto_inicial():
    print(
        "Estamos ubicados en Washington D.C., Estados Unidos. Hace 200 años, una guerra nuclear dejó irradiado e inhabitable el mundo exterior. " #linea1
        "Con suerte, tu familia y varios elegidos más pudieron sobrevivir entrando en un refugio. Han pasado 200 años y eres uno de los descendientes " #linea2
        "de los supervivientes. Sin embargo, algo está mal: las luces dejaron de funcionar y la puerta del búnker se ha abierto. " #linea3
        "Quizás alguien no soportó vivir toda su vida en un búnker o simplemente enloqueció. " #linea4
        "Lo único que sabemos es que el sistema de electricidad se ha averiado y muchas puertas automaticas ahora deberan ser abiertas manualmente, " #linea5
        "Estabas en tu turno rutinario por los pasillos, cuando decidiste revisar el cuarto de limpieza, que lastima que se te haya caido la llave tras iniciar la crisis," #linea6
        "Por ahora lo mejor sera salir del bunker y talvez descubrir porque sucedio todo esto \n\n" #linea7
    )
    run("titulo.wav",0)

    print(
        "cuarto_de_limpieza: Estás en un pequeño cuarto de limpieza. Al norte está la entrada al Pasillo Inicial (2)." #linea8
    )
    run("newquest.wav",0)

ubicacion_actual = "cuarto_de_limpieza"
juego_terminado = False
inventario = ["Pistola"]
notas_recogidas = 0

# Sección 2: Descripciones y Movimientos

descripciones = {
    "cuarto_de_limpieza": "Estás en un pequeño cuarto de limpieza. Al norte está la entrada al Pasillo Inicial (2).", #linea9
    "pasillo_1": "Estás en un largo pasillo oscuro. Al sur está el Cuarto de Limpieza (1), al norte el Pasillo Principal (1), y al este una Habitación Oscura (1).", #linea10
    "habitacion_bala": "Una pequeña habitación oscura. Al oeste está el Pasillo Inicial (1).", #linea11
    "pasillo_2": "Continúas en el pasillo. Al sur está el Pasillo Inicial (1), al norte el Pasillo Final (2), al oeste un pasillo manchado de sangre (1) y al este una Sala Misteriosa (1).", #linea12
    "sala_palanca": "Una sala misteriosa con una palanca en el centro. Al oeste está el Pasillo Principal (1).",#linea13
    "pasillo_ghoul": "Un pasillo estrecho. Al este está el Pasillo Principal (1) y al norte una Sala con una preocupante criatura (3). Algo peligroso te espera adelante. Necesitas estar armado para continuar",#linea14
    "sala_ghoul": "Una sala oscura. Al sur está el Pasillo Estrecho (1).", #linea15
    "pasillo_final": "Este es el pasillo que conduce a la salida. Al sur está el Pasillo Principal (1), y al norte la Salida (3).", #linea16
    "salida": "Finalmente llegaste a la salida del búnker. Al sur está el Pasillo Final (1)." #linea17
}


# Números que simbolizan el tipo de sala:
# 0: Habitación inaccesible
# 1: Habitación accesible
# 2: Habitación que requiere palanca
# 3: Habitación accesible pero con un evento o requerimiento especial
# 4: Habitación que requiere llave

movimientos = {
    "cuarto_de_limpieza": {
        "norte": ("pasillo_1", 4), # Requiere la llave para avanzar
        "este": ("", 0),
        "oeste": ("", 0),
        "sur": ("", 0)
    },
    "pasillo_1": {
        "sur": ("cuarto_de_limpieza", 1),
        "norte": ("pasillo_2", 1),
        "este": ("habitacion_bala", 1),
        "oeste": ("", 0)
    },
    "habitacion_bala": {
        "oeste": ("pasillo_1", 1),
        "norte": ("", 0),
        "sur": ("", 0),
        "este": ("", 0)
    },
    "pasillo_2": {
        "sur": ("pasillo_1", 1),
        "norte": ("pasillo_final", 2),  # Requiere la palanca para avanzar
        "este": ("sala_palanca", 1),
        "oeste": ("pasillo_ghoul", 1)
    },
    "sala_palanca": {
        "oeste": ("pasillo_2", 1),
        "norte": ("", 0),
        "sur": ("", 0),
        "este": ("", 0)
    },
    "pasillo_ghoul": {
        "sur": ("", 0),
        "norte": ("sala_ghoul", 3),  # Se necesita la pistola y bala
        "este": ("pasillo_2", 1),
        "oeste": ("", 0)
    },
    "sala_ghoul": {
        "sur": ("pasillo_ghoul", 1),
        "norte": ("", 0),
        "este": ("", 0),
        "oeste": ("", 0)
    },
    "pasillo_final": {
        "sur": ("pasillo_2", 1),
        "norte": ("salida", 3),  # El final depende de las notas recogidas
        "este": ("", 0),
        "oeste": ("", 0)
    },
    "salida": {
        "sur": ("pasillo_final", 1),
        "norte": ("", 0),
        "este": ("", 0),
        "oeste": ("", 0)
    }
}

# Sección 3: Funciones de Movimiento y Exploración

def mover_jugador(direccion):
    global ubicacion_actual
    if direccion in movimientos[ubicacion_actual]:
        destino, tipo_habitacion = movimientos[ubicacion_actual][direccion]
        run("caminar.wav",5)
        if tipo_habitacion == 0:
            print("Un gran muro de metal te cubre el paso.") #linea18
            run("murometal.wav",5)
        elif tipo_habitacion == 4 and "Llave" not in inventario:
            print("La puerta está cerrada. Necesitas una llave para abrirla.") #linea19
            run("puertacerrada.wav",2)
        elif tipo_habitacion == 2 and "Palanca" not in inventario:
            print("La puerta está cerrada. Necesitas una palanca para abrirla.") #linea20
            run("puertacerrada.wav",2)
        else:
            ubicacion_actual = destino
            print(descripciones[ubicacion_actual])
            if ubicacion_actual == "sala_ghoul" and "Pistola" in inventario and "Bala" in inventario:
                print(
                    "Disparaste al ghoul con la pistola. Puedes recoger lo que protegía." #linea21
                )
                run("disparo.wav",7)
            elif ubicacion_actual == "sala_ghoul" and "Bala" not in inventario:
                print("Logras ver con claridad a la criatura que antes no podias, no era un humano, ni un cadaver, simplemente el fin de tu vida.\n") #linea22
                run("ghoul.wav",7)
                print("El ghoul te ataca... y mueres.") #linea23
                run("muerte.wav",2)
                global juego_terminado
                juego_terminado = True
    else:
        print("No puedes moverte en esa dirección.") #linea24
        run("error.wav",0)
# Sección 4: Interacción con Objetos y Manejo del Inventario

def examinar_objeto(objeto):
    if objeto == ubicacion_actual:
        # Verificar qué objetos hay en la sala actual
        objetos_en_sala = {
            "cuarto_de_limpieza": ["Llave"], 
            "habitacion_bala": ["Bala"],
            "sala_palanca": ["Palanca"],
            "pasillo_1": ["Nota1"],
            "pasillo_2": ["Nota2"],
            "sala_ghoul": ["Nota3"],
            "pasillo_ghoul": ["Nota4"],
            "pasillo_final": ["Nota5"]
        }

        if ubicacion_actual in objetos_en_sala:
            print(f"En esta sala puedes ver: {', '.join(objetos_en_sala[ubicacion_actual])}.") #linea25 (aqui pueden haber hasta 8 variaciones)
            run("buscar.wav",0)
        else:
            print("No hay nada interesante aquí.") #linea26
            run("nada.wav",2)
    else:
        # Verificar objetos específicos
        if ubicacion_actual == "cuarto_de_limpieza" and objeto.lower() == "llave":
            print(
                "Es una pequeña llave oxidada, parece que puede abrir alguna puerta cercana." #linea27
            )
            run("llave.wav",1)
        elif ubicacion_actual == "sala_palanca" and objeto.lower() == "palanca":
            print(
                "Una palanca de metal. Probablemente sea útil para abrir algo bloqueado." #linea28
            )
            run("palanca.wav",1)
        elif ubicacion_actual == "habitacion_bala" and objeto.lower() == "bala":
            print(
                "Una bala solitaria en el suelo. Parece que alguien la dejó caer aquí." #linea29
            )
            run("bala.wav",1)
        elif ubicacion_actual == "pasillo_1" and objeto.lower() == "nota1":
            print(
                "Nota 1: 'Este lugar se está desmoronando, la puerta del búnker se está debilitando...'" #linea30
            )
            run("nota.wav",1)
        elif ubicacion_actual == "pasillo_2" and objeto.lower() == "nota2":
            print(
                "Nota 2: 'La gente está empezando a volverse loca, uno de ellos dijo que la salida está cerca...'" #linea31
            )
            run("nota.wav",1)
        elif ubicacion_actual == "sala_ghoul" and objeto.lower() == "nota3":
            print(
                "Nota 3: 'Vi a papá hablando con alguien, pero no hay nadie más aquí...'" #linea32
            )
            run("nota.wav",1)
        elif ubicacion_actual == "pasillo_ghoul" and objeto.lower() == "nota4":
            print(
                "Nota 4: 'Papá está tramando algo, lo sé, no puedo confiar en él...'" #linea33
            )
            run("nota.wav",1)
        elif ubicacion_actual == "pasillo_final" and objeto.lower() == "nota5":
            print(
                "Nota 5: 'Todo esto es su culpa, fue él quien causó todo esto...'" #linea34
            ) 
            run("nota.wav",1)
        else:
            print("No hay nada interesante aquí.") #linea35
            run("nada.wav",2)

def recoger_objeto(objeto): #linea36 (aqui pueden haber hasta 8 variaciones)
    global notas_recogidas
    if ubicacion_actual == "cuarto_de_limpieza" and objeto.lower() == "llave":
        print("Has recogido la Llave.") 
        inventario.append("Llave")
        run("recoger.wav",2)
    elif ubicacion_actual == "habitacion_bala" and objeto.lower() == "bala":
        print("Has recogido la Bala.")
        inventario.append("Bala")
        run("recoger.wav",2)
    elif ubicacion_actual == "sala_palanca" and objeto.lower() == "palanca":
        print("Has recogido la Palanca.")
        inventario.append("Palanca")
        run("recoger.wav",2)
    elif objeto.lower().startswith("nota"):
        if objeto.lower() not in inventario:
            print(f"Has recogido la {objeto.capitalize()}.")
            inventario.append(objeto.capitalize())
            notas_recogidas += 1
            run("recoger.wav",2)
    else:
        print("No hay nada que recoger aquí.") #linea37
        run("nada.wav",2)

# Sección 5: Mecánica de Finales Alternativos

def finalizar_juego():
    global juego_terminado
    if notas_recogidas == 5:
        print(
            "Has encontrado todas las notas y descubres la verdad sobre lo que pasó. " #linea38
            "En la salida, te enfrentas a una difícil decisión: confrontar a tu padre o perdonarlo." #linea39
        )
        run("suspenso.wav",0)
        eleccion = input("¿Qué decides hacer? (confrontar/perdonar): ").lower() #linea40
        run("eleccion.wav",0)
        if eleccion == "confrontar":
            print(
                "Confrontas a tu padre y descubres que él fue el culpable de la tragedia, simplemente estaba cansado de vivir como una rata" #linea41
                "Decides enfrentarlo y, al final, muere. ¡Has conseguido el final bueno!" #linea42
            )
            run("pelea.wav",0)
            print(
                "\nEpílogo3:\n" #linea43
                "Después de confrontar a tu padre, la verdad sale a la luz. La comunidad en el búnker te apoya y te ayuda a " #linea44
                "reconstruir una nueva vida fuera del refugio. Aunque el pasado siempre estará presente, encuentras consuelo en " #linea45
                "saber que hiciste lo correcto. Tu valentía y determinación inspiran a otros a enfrentar sus propios miedos " #linea46
                "y a buscar la verdad, sin importar cuán dolorosa sea." #linea47
            )
            run("happyending.wav",0)
        elif eleccion == "perdonar":
            print(
                "Decides perdonar a tu padre y lo ayudas a escapar. " #linea48
                "Aunque la verdad es difícil de soportar, optas por la reconciliación. ¡Has conseguido el final neutral!" #linea49
            )
            run("paz.wav",0)
            print( 
                "\nEpílogo2:\n" #linea50
                "Tu decisión de perdonar a tu padre lleva a una nueva esperanza para ambos. Juntos, intentan construir una " #linea51
                "vida mejor en un mundo que ha sido devastado. Aunque el peso de la verdad sigue siendo una carga, el acto de " #linea52
                "perdón y la reconciliación traen una nueva oportunidad para sanar. Ambos encuentran paz en su relación, " #linea53
                "a cambio unicamente sacrificaron la vida pacifica de todos en el bunker. No todos pueden ser felices" #linea54
                )
            run("neutralending.wav",0)
        else:
            print("No tomaste ninguna decisión válida, logras ver como tu padre se marcha mientras cae sobre ti el peso de no haber hecho nada, Has conseguido el final más peye, felicitaciones supongo ...") #linea55
            juego_terminado = True
            run("peyeending.wav",0)
    else:
        print(
            "No encontraste todas las notas, así que nunca descubriste la verdad. " #linea56
            "Escapas, pero con una sensación de vacío y duda. ¡Has conseguido el final malo!" #linea57
        )
        run("crisis.wav",0)
        print(
            "\nEpílogo1:\n" #linea58
            "A pesar de tu escape, la falta de respuestas te persigue. El mundo exterior sigue siendo un misterio, y el " #linea59
            "peso de no haber descubierto toda la verdad te deja una sensación de incompletitud. La experiencia en el búnker " #linea60
            "te ha cambiado para siempre, y aunque estás libre, el vacío de no haber logrado encontrar todas las respuestas " #linea61
            "es un recordatorio constante de las decisiones que no pudiste tomar " #linea62
            )
        run("desierto",0)
    juego_terminado = True

# Sección 6: Ayuda y Función Principal

def mostrar_ayuda():
    print(
        "Comandos disponibles:\n"
        "- 'mover [norte/sur/este/oeste]': Para moverte entre habitaciones.\n" #linea63
        "- 'examinar [nombre del objeto]': Para examinar objetos en la habitación actual.\n" #linea64
        "- 'recoger [nombre del objeto]': Para recoger un objeto en la habitación actual.\n" #linea65
        "- 'examinar [nombre de la sala actual]': Para ver qué objetos hay en la sala actual.\n" #linea66
        "- 'ayuda': Muestra esta ayuda.\n\n" #linea67
        "Descripción de los números de las salas:\n" #linea68
        "1: Habitación accesible.\n" #linea69
        "2: Habitación que requiere un objeto específico para avanzar.\n" #linea70
        "3: Habitación peligrosa mejor estar armados.\n" #linea71
    )
    run("help.wav",0)

def jugar():
    mostrar_contexto_inicial()
    while not juego_terminado:
        comando = input("\n¿Qué quieres hacer? ").lower().split() #linea72
        if len(comando) == 2:
            accion, objeto_o_direccion = comando
            if accion == "mover":
                mover_jugador(objeto_o_direccion)
            elif accion == "examinar":
                examinar_objeto(objeto_o_direccion)
            elif accion == "recoger":
                recoger_objeto(objeto_o_direccion)
            else:
                print("Comando no reconocido.") #linea73
                run("error.wav",0)
        elif len(comando) == 1:
            if comando[0] == "ayuda":
                mostrar_ayuda()
            elif comando[0] == "salir":
                print("Gracias por jugar. ¡Hasta la próxima!") #linea74
                run("bye.wav",0)
                break
            elif comando[0] == "examinar":
                examinar_objeto(ubicacion_actual)
            else:
                print("Comando no reconocido.") #linea75
                run("error.wav",0)
        else:
            print("Comando no reconocido.") #linea76
            run("error.wav",0)

        if ubicacion_actual == "salida":
            finalizar_juego()

# Ejecución del juego
jugar()