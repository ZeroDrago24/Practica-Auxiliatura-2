class Persona:
    def __init__(self, ci, nombre, ape, cel, fecha_nac):
        self.ci = ci
        self.nombre = nombre
        self.ape = ape
        self.cel = cel
        self.fecha_nac = fecha_nac

    def edad(self):
        return 2025 - self.fecha_nac

class Estudiante(Persona):
    guardar = []

    def __init__(self, ci, nombre, ape, cel, fecha_nac, ru, fecha_ingreso, semestre):
        super().__init__(ci, nombre, ape, cel, fecha_nac)
        self.ru = ru
        self.fecha_ingreso = fecha_ingreso
        self.semestre = semestre

    def guardarestudiante(self):
        Estudiante.guardar.append(self)

    @staticmethod
    def mostrar():
        for est in Estudiante.guardar:
            print(f"El estudiante {est.nombre} {est.ape}, celular {est.cel}, "
                  f"nacido en {est.fecha_nac}, RU {est.ru}, ingresó en {est.fecha_ingreso}, "
                  f"semestre {est.semestre}.")

    @staticmethod
    def mostrarmayor():
        print("\nEstudiantes mayores de 25 años:")
        for est in Estudiante.guardar:
            if est.edad() > 25:
                print(f"{est.nombre} {est.ape}, edad: {est.edad()}, semestre: {est.semestre}")

class Docente(Persona):
    guardardoc = []

    def __init__(self, ci, nombre, ape, cel, fecha_nac, nit, profesion, especialidad):
        super().__init__(ci, nombre, ape, cel, fecha_nac)
        self.nit = nit
        self.profesion = profesion
        self.especialidad = especialidad

    def guardarDocente(self):
        Docente.guardardoc.append(self)

    @staticmethod
    def mostrardoc():
        for doc in Docente.guardardoc:
            print(f"{doc.nombre} {doc.ape}, celular: {doc.cel}, {doc.profesion}, {doc.especialidad}")

    @staticmethod
    def mostrardocenteIngenieria():
        print("\nDocentes de Ingeniería:")
        for doc in Docente.guardardoc:
            if doc.profesion in ["Ingeniero", "Ingeniera"]:
                print(f"{doc.nombre} {doc.ape}, celular: {doc.cel}, {doc.profesion}, {doc.especialidad}")

def mostrar_mismo_apellido():
    print("\nEstudiantes y Docentes con el mismo apellido:")
    hayCoincidencia = False
    for est in Estudiante.guardar:
        for doc in Docente.guardardoc:
            if est.ape == doc.ape:
                print(f"- {est.nombre} {est.ape} (Estudiante) y {doc.nombre} {doc.ape} (Docente)")
                hayCoincidencia = True
    if not hayCoincidencia:
        print("No se encontraron coincidencias.")

# Datos de prueba
e1 = Estudiante("123", "Luis", "López", "789456", 1990, "RU123", 2021, 7)
e2 = Estudiante("456", "María", "Mamani", "123789", 1999, "RU456", 2022, 5)
e1.guardarestudiante()
e2.guardarestudiante()

Estudiante.mostrar()
Estudiante.mostrarmayor()

d1 = Docente("789", "Carlos", "López", "987654", 1980, "NIT123", "Ingeniero", "Sistemas")
d2 = Docente("321", "Ana", "Rojas", "654987", 1985, "NIT456", "Licenciada", "Matemáticas")
d3 = Docente("654", "Jorge", "Mamani", "321654", 1975, "NIT789", "Doctor", "Física")
d4 = Docente("987", "Lucía", "Quiroz", "963852", 1990, "NIT321", "Ingeniera", "Electrónica")
d1.guardarDocente()
d2.guardarDocente()
d3.guardarDocente()
d4.guardarDocente()

Docente.mostrardoc()
Docente.mostrardocenteIngenieria()
mostrar_mismo_apellido()
