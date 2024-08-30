# Sección 1: Contexto Inicial y Configuración

def mostrar_contexto_inicial():
    print(
        "Estamos ubicados en Washington D.C., Estados Unidos. Hace 200 años, una guerra nuclear dejó irradiado e inhabitable el mundo exterior. "
        "Con suerte, tu familia y varios elegidos más pudieron sobrevivir entrando en un refugio. Han pasado 200 años y eres uno de los descendientes "
        "de los supervivientes. Sin embargo, algo está mal: las luces dejaron de funcionar y la puerta del búnker se ha abierto. "
        "Quizás alguien no soportó vivir toda su vida en un búnker o simplemente enloqueció. Lo único que sabemos es que el sistema de electricidad "
        "se ha averiado y solo cuentas con 60 minutos de batería, tras lo cual, si no haces algo, no podrás escapar. "
        "Eres el último en el refugio. A tu amigo George le pareció divertido encerrarte en el pequeño cuarto de limpieza, "
        "pero lo que no sabe es que, a pesar de no haber luz, tienes un gran oído, el mejor.\n\n"
        "cuarto_de_limpieza: Estás en un pequeño cuarto de limpieza. Al norte está la entrada al Pasillo Inicial (2)."
    )

ubicacion_actual = "cuarto_de_limpieza"
juego_terminado = False
inventario = ["Pistola"]
notas_recogidas = 0

# Sección 2: Descripciones y Movimientos

descripciones = {
    "cuarto_de_limpieza": "Estás en un pequeño cuarto de limpieza. Al norte está la entrada al Pasillo Inicial (2).",
    "pasillo_1": "Estás en un largo pasillo oscuro. Al sur está el Cuarto de Limpieza (1), al norte el Pasillo Principal (1), y al este una Habitación Oscura (1).",
    "habitacion_bala": "Una pequeña habitación oscura. Al oeste está el Pasillo Inicial (1).",
    "pasillo_2": "Continúas en el pasillo. Al sur está el Pasillo Inicial (1), al norte el Pasillo Final (2), y al este una Sala Misteriosa (1).",
    "sala_palanca": "Una sala misteriosa con una palanca en el centro. Al oeste está el Pasillo Principal (1).",
    "pasillo_ghoul": "Un pasillo estrecho. Al sur está el Pasillo Principal (1) y al norte una Sala Oscura (3).",
    "sala_ghoul": "Una sala oscura. Al sur está el Pasillo Estrecho (1).",
    "pasillo_final": "Este es el pasillo que conduce a la salida. Al sur está el Pasillo Principal (1), y al norte la Salida (3).",
    "salida": "Finalmente llegaste a la salida del búnker. Al sur está el Pasillo Final (1)."
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
        "oeste": ("", 0)
    },
    "sala_palanca": {
        "oeste": ("pasillo_2", 1),
        "norte": ("", 0),
        "sur": ("", 0),
        "este": ("", 0)
    },
    "pasillo_ghoul": {
        "sur": ("pasillo_2", 1),
        "norte": ("sala_ghoul", 3),  # Se necesita la pistola y bala
        "este": ("", 0),
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
        if tipo_habitacion == 0:
            print("Un gran muro de metal te cubre el paso.")

        elif tipo_habitacion == 4 and "Llave" not in inventario:
            print("La puerta está cerrada. Necesitas una llave para abrirla.")
            
        elif tipo_habitacion == 2 and "Palanca" not in inventario:
            print("La puerta está cerrada. Necesitas una palanca para abrirla.")
        
        elif tipo_habitacion == 3 and ("Pistola" not in inventario or "Bala" not in inventario):
            print("Algo peligroso te espera adelante. Necesitas estar armado para continuar.")
        else:
            ubicacion_actual = destino
            print(descripciones[ubicacion_actual])
            if ubicacion_actual == "sala_ghoul" and "Pistola" in inventario and "Bala" in inventario:
                print(
                    "Disparaste al ghoul con la pistola. Puedes recoger lo que protegía."
                )
            elif ubicacion_actual == "sala_ghoul" and "Pistola" not in inventario:
                print("El ghoul te ataca... y mueres.")
                global juego_terminado
                juego_terminado = True
    else:
        print("No puedes moverte en esa dirección.")

# Sección 4: Interacción con Objetos y Manejo del Inventario

def examinar_objeto(objeto):
    if objeto == ubicacion_actual:
        # Verificar qué objetos hay en la sala actual
        objetos_en_sala = {
            "cuarto_de_limpieza": ["Llave"],
            "habitacion_bala": ["Bala"],
            "sala_palanca": ["Palanca", "Nota3"],
            "pasillo_1": ["Nota1"],
            "pasillo_2": ["Nota2"],
            "pasillo_ghoul": ["Nota4"],
            "salida": ["Nota5"]
        }

        if ubicacion_actual in objetos_en_sala:
            print(f"En esta sala puedes ver: {', '.join(objetos_en_sala[ubicacion_actual])}.")
        else:
            print("No hay nada interesante aquí.")
    else:
        # Verificar objetos específicos
        if ubicacion_actual == "cuarto_de_limpieza" and objeto.lower() == "llave":
            print(
                "Es una pequeña llave oxidada, parece que puede abrir alguna puerta cercana."
            )
        elif ubicacion_actual == "sala_palanca" and objeto.lower() == "palanca":
            print(
                "Una palanca de metal. Probablemente sea útil para abrir algo bloqueado."
            )
        elif ubicacion_actual == "habitacion_bala" and objeto.lower() == "bala":
            print(
                "Una bala solitaria en el suelo. Parece que alguien la dejó caer aquí."
            )
        elif ubicacion_actual == "pasillo_1" and objeto.lower() == "nota1":
            print(
                "Nota 1: 'Este lugar se está desmoronando, la puerta del búnker se está debilitando...'"
            )
        elif ubicacion_actual == "pasillo_2" and objeto.lower() == "nota2":
            print(
                "Nota 2: 'La gente está empezando a volverse loca, uno de ellos dijo que la salida está cerca...'"
            )
        elif ubicacion_actual == "sala_palanca" and objeto.lower() == "nota3":
            print(
                "Nota 3: 'Vi a papá hablando con alguien, pero no hay nadie más aquí...'"
            )
        elif ubicacion_actual == "pasillo_ghoul" and objeto.lower() == "nota4":
            print(
                "Nota 4: 'Papá está tramando algo, lo sé, no puedo confiar en él...'"
            )
        elif ubicacion_actual == "salida" and objeto.lower() == "nota5":
            print(
                "Nota 5: 'Todo esto es su culpa, fue él quien causó todo esto...'")
        else:
            print("No hay nada interesante aquí.")


def recoger_objeto(objeto):
    global notas_recogidas
    if ubicacion_actual == "cuarto_de_limpieza" and objeto.lower() == "llave":
        print("Has recogido la Llave.")
        inventario.append("Llave")
    elif ubicacion_actual == "habitacion_bala" and objeto.lower() == "bala":
        print("Has recogido la Bala.")
        inventario.append("Bala")
    elif ubicacion_actual == "sala_palanca" and objeto.lower() == "palanca":
        print("Has recogido la Palanca.")
        inventario.append("Palanca")
    elif objeto.lower().startswith("nota"):
        if objeto.lower() not in inventario:
            print(f"Has recogido la {objeto.capitalize()}.")
            inventario.append(objeto.capitalize())
            notas_recogidas += 1
    else:
        print("No hay nada que recoger aquí.")

# Sección 5: Mecánica de Finales Alternativos

def finalizar_juego():
    global juego_terminado
    if notas_recogidas == 5:
        print(
            "Has encontrado todas las notas y descubres la verdad sobre lo que pasó. "
            "En la salida, te enfrentas a una difícil decisión: confrontar a tu padre o perdonarlo."
        )
        eleccion = input("¿Qué decides hacer? (confrontar/perdonar): ").lower()
        if eleccion == "confrontar":
            print(
                "Confrontas a tu padre y descubres que él fue el culpable de la tragedia. "
                "Decides enfrentarlo y, al final, encuentras la paz. ¡Has conseguido el final bueno!"
            )
        elif eleccion == "perdonar":
            print(
                "Decides perdonar a tu padre y lo ayudas a escapar. "
                "Aunque la verdad es difícil de soportar, optas por la reconciliación. ¡Has conseguido el final bueno!"
            )
        else:
            print("No tomaste ninguna decisión válida y el tiempo se agotó.")
            juego_terminado = True
    else:
        print(
            "No encontraste todas las notas, así que nunca descubriste la verdad. "
            "Escapas, pero con una sensación de vacío y duda. ¡Has conseguido el final malo!"
        )
    juego_terminado = True

# Sección 6: Ayuda y Función Principal

def mostrar_ayuda():
    print(
        "Comandos disponibles:\n"
        "- 'mover [norte/sur/este/oeste]': Para moverte entre habitaciones.\n"
        "- 'examinar [nombre del objeto]': Para examinar objetos en la habitación actual.\n"
        "- 'recoger [nombre del objeto]': Para recoger un objeto en la habitación actual.\n"
        "- 'examinar [nombre de la sala actual]': Para ver qué objetos hay en la sala actual.\n"
        "- 'ayuda': Muestra esta ayuda.\n\n"
        "Descripción de los números de las salas:\n"
        "1: Habitación accesible.\n"
        "2: Habitación que requiere un objeto específico para avanzar.\n"
        "3: Habitación peligrosa mejor estar armados.\n"
    )

def jugar():
    mostrar_contexto_inicial()
    while not juego_terminado:
        comando = input("\n¿Qué quieres hacer? ").lower().split()
        if len(comando) == 2:
            accion, objeto_o_direccion = comando
            if accion == "mover":
                mover_jugador(objeto_o_direccion)
            elif accion == "examinar":
                examinar_objeto(objeto_o_direccion)
            elif accion == "recoger":
                recoger_objeto(objeto_o_direccion)
            else:
                print("Comando no reconocido.")
        elif len(comando) == 1:
            if comando[0] == "ayuda":
                mostrar_ayuda()
            elif comando[0] == "salir":
                print("Gracias por jugar. ¡Hasta la próxima!")
                break
            elif comando[0] == "examinar":
                examinar_objeto(ubicacion_actual)
            else:
                print("Comando no reconocido.")
        else:
            print("Comando no reconocido.")

        if ubicacion_actual == "salida":
            finalizar_juego()

# Ejecución del juego
jugar()