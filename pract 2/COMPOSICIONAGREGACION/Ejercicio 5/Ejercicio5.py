class Jugador:
    def __init__(self, nombre, numero, posicion):
        self.nombre = nombre
        self.numero = numero
        self.posicion = posicion

    def mostrar_info(self):
        return f"{self.nombre} {self.numero} {self.posicion}"


class Portero(Jugador):
    def __init__(self, nombre, numero, posicion, habilidad):
        super()._init_(nombre, numero, posicion)
        self.atajada = habilidad

    def mostrar_info(self):
        return f"{super().mostrar_info()} - Habilidad: {self.atajada}"


class Defensa(Jugador):
    def __init__(self, nombre, numero, posicion, habilidad):
        super()._init_(nombre, numero, posicion)
        self.marcaje = habilidad

    def mostrar_info(self):
        return f"{super().mostrar_info()} - Habilidad: {self.marcaje}"


class Mediocampista(Jugador):
    def __init__(self, nombre, numero, posicion, habilidad):
        super().__init__(nombre, numero, posicion)
        self.pases = habilidad

    def mostrar_info(self):
        return f"{super().mostrar_info()} - Habilidad: {self.pases}"


class Delantero(Jugador):
    def __init__(self, nombre, numero, posicion, habilidad):
        super()._init_(nombre, numero, posicion)
        self.goles = habilidad

    def mostrar_info(self):
        return f"{super().mostrar_info()} - Habilidad: {self.goles}"


class Equipo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.jugadores = []

    def agregarJugador(self, nombre, numero, posicion, habilidad):
        if posicion == "portero":
            jugador = Portero(nombre, numero, posicion, habilidad)
        elif posicion == "defensa":
            jugador = Defensa(nombre, numero, posicion, habilidad)
        elif posicion == "mediocampista":
            jugador = Mediocampista(nombre, numero, posicion, habilidad)
        elif posicion == "delantero":
            jugador = Delantero(nombre, numero, posicion, habilidad)
        else:
            jugador = Jugador(nombre, numero, posicion)  
            self.jugadores.append(jugador)

    def mostrar(self):
        print(f"Equipo: {self.nombre}")
        print("Jugadores:")
        for jugador in self.jugadores:
            print(jugador.mostrar_info())


# Ejemplo de uso
equipo = Equipo("Always Ready")
equipo.agregarJugador("Juan", 1, "Portero", "Atajadas")
equipo.agregarJugador("Pedro", 3, "Defensa", "Marcaje")
equipo.agregarJugador("Carlos", 5, "Mediocampista", "Pases")
equipo.agregarJugador("Luis", 9, "Delantero", "Goles")
equipo.agregarJugador("Alex", 7, "Suplente", "")  
equipo.mostrar()