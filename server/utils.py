"""
Utils con todas las clases necesarias para correr
el servidor
    - Mazo
    - Carta
"""
# [TODO] 02 February 2020 implementar logging

import json
from random import shuffle, randint


class Sala:
    CARTAS_NEGRAS_DIR = "texto_cartas/cartas_negras.json"
    CARTAS_BLANCAS_DIR = "texto_cartas/cartas_blancas.json"

    def __init__(self):
        self.hash = randint(
            100, 999
        )  # [TODO] 02 February 2020 Esto deberia ser un hash
        self.mazo_negro = Mazo(self.CARTAS_NEGRAS_DIR)
        self.mazo_blanco = Mazo(self.CARTAS_BLANCAS_DIR)
        self.jugadores = []

    def agarrar_negra(self):
        return self.mazo_negro.agarrar()

    def agarrar_blanca(self):
        return self.mazo_blanco.agarrar()

    def agregar_jugador(self, jugador):
        print(f"{jugador.nombre} se unio a la sala")
        self.jugadores.append(jugador)


class Jugador:
    """
    Clase que maneja la logica de un jugador
    """

    def __init__(self, nombre):
        self.hash = "123"  # [TODO] 02 February 2020 generar un hash para cada jugador
        self.nombre = nombre
        self.puntos = 0


class Mazo:
    """
    Clase que maneja la logica de los mazos.
    Estos pueden ser:
        - Blanco (cartas de los jugadores)
        - Negro (cartas consignas)
    """

    # [TODO] 02 February 2020 Cual seria la mejor forma de hacer cada mazo?
    def __init__(self, fn):
        self.cartas = []
        # Cargar cartas desde el archivo cartas
        with open(fn, "r") as file:
            textos = json.load(file)
        for t in textos:
            self.cartas.append(Carta(t))
        shuffle(self.cartas)

    def agarrar(self):
        return self.cartas.pop()


class Carta:
    """
    Clase que maneja la logica de las cartas
    """

    def __init__(self, texto):
        self.texto = texto


if __name__ == "__main__":
    salita = Sala()
    print("Sala creada")

    player = Jugador("Eric")
    print(f"Jugador {player.nombre} creado")

    salita.agregar_jugador(player)

    print(salita.agarrar_blanca().texto)
    print(salita.agarrar_negra().texto)
