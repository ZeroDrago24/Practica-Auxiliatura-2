class Estudiante:
    def __init__(self, nombre, carrera, semestre):
        self.nombre = nombre
        self.carrera = carrera
        self.semestre = semestre

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Carrera: {self.carrera}, Semestre: {self.semestre}")

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_carrera(self):
        return self.carrera

    def set_carrera(self, carrera):
        self.carrera = carrera

    def get_semestre(self):
        return self.semestre

    def set_semestre(self, semestre):
        self.semestre = semestre


class Universidad:
    def __init__(self, nombre):
        self.nombre = nombre
        self.estudiantes = []

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)

    def mostrar_universidad(self):
        print(f"\nUniversidad: {self.nombre}")
        print("Estudiantes:")
        for estudiante in self.estudiantes:
            estudiante.mostrar_info()

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_estudiantes(self):
        return self.estudiantes


# Crear estudiantes
e1 = Estudiante("Carlos López", "Informática", 5)
e2 = Estudiante("Lucía Pérez", "Electrónica", 3)
e3 = Estudiante("Mario Rojas", "Mecatrónica", 2)

# Crear universidad
u1 = Universidad("Universidad Técnica de Bolivia")

# Agregar estudiantes a la universidad
u1.agregar_estudiante(e1)
u1.agregar_estudiante(e2)
u1.agregar_estudiante(e3)

# Mostrar información de la universidad y sus estudiantes
u1.mostrar_universidad()
