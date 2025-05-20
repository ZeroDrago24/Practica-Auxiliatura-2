class Habitacion:
    def __init__(self, nombre: str, tamaño: float):
        self.nombre = nombre
        self.tamaño = tamaño

    def mostrar(self):
        return f"{self.nombre} - {self.tamaño} m²"

class Casa:
    def __init__(self, direccion: str):
        self.direccion = direccion
        self.habitaciones = []  # plural para lista

    def agregarHab(self, nombre, tamaño):
        habitacion = Habitacion(nombre, tamaño)  # la casa crea la habitación (composición)
        self.habitaciones.append(habitacion)

    def muestra(self):
        print(f"La casa con la direccion {self.direccion}")
        print("Con las habitaciones:")
        for i in range(len(self.habitaciones)):
            print(self.habitaciones[i].mostrar())

# Uso:
casa1 = Casa("Edificio Central")
casa1.agregarHab("Planta alta", 45.0)
casa1.agregarHab("Sala", 23.5)
casa1.muestra()