class Empleado:
    def __init__(self, nombre, apellido, salario_base, años_antiguedad):
        self.nombre = nombre
        self.apellido = apellido
        self.salario_base = salario_base
        self.años_antiguedad = años_antiguedad

    def calcular_salario(self):
        bono = self.salario_base * 0.05 * self.años_antiguedad
        return self.salario_base + bono

    def get_nombre(self):
        return self.nombre

    def get_apellido(self):
        return self.apellido

    def get_salario_base(self):
        return self.salario_base

    def get_años_antiguedad(self):
        return self.años_antiguedad


class Gerente(Empleado):
    gerentes = []

    def __init__(self, nombre, apellido, salario_base, años_antiguedad, departamento, bono_gerencial):
        super().__init__(nombre, apellido, salario_base, años_antiguedad)
        self.departamento = departamento
        self.bono_gerencial = bono_gerencial
        Gerente.gerentes.append(self)

    def calcular_salario(self):
        salario_base_total = super().calcular_salario()
        return salario_base_total + self.bono_gerencial

    def get_bono_gerencial(self):
        return self.bono_gerencial

    def get_departamento(self):
        return self.departamento


class Desarrollador(Empleado):
    desarrolladores = []

    def __init__(self, nombre, apellido, salario_base, años_antiguedad, lenguaje_programacion, horas_extras):
        super().__init__(nombre, apellido, salario_base, años_antiguedad)
        self.lenguaje_programacion = lenguaje_programacion
        self.horas_extras = horas_extras
        Desarrollador.desarrolladores.append(self)

    def calcular_salario(self):
        salario_base_total = super().calcular_salario()
        monto_horas_extras = self.horas_extras * 50  # Por ejemplo, 50 por hora extra
        return salario_base_total + monto_horas_extras

    def get_horas_extras(self):
        return self.horas_extras

    def get_lenguaje_programacion(self):
        return self.lenguaje_programacion


# Crear instancias
g1 = Gerente("Carlos", "Lopez", 5000, 10, "Sistemas", 1200)
g2 = Gerente("Lucia", "Perez", 4000, 5, "Recursos Humanos", 800)

d1 = Desarrollador("Mario", "Rojas", 3000, 4, "Python", 12)
d2 = Desarrollador("Ana", "Torrez", 3200, 6, "Java", 8)

# Mostrar salarios calculados
print(f"{g1.get_nombre()} {g1.get_apellido()} - Salario: {g1.calcular_salario()}")
print(f"{g2.get_nombre()} {g2.get_apellido()} - Salario: {g2.calcular_salario()}")

print(f"{d1.get_nombre()} {d1.get_apellido()} - Salario: {d1.calcular_salario()}")
print(f"{d2.get_nombre()} {d2.get_apellido()} - Salario: {d2.calcular_salario()}")

# Mostrar gerentes con bono > 1000
print("\nGerentes con bono mayor a 1000:")
for g in Gerente.gerentes:
    if g.get_bono_gerencial() > 1000:
        print(f"{g.get_nombre()} {g.get_apellido()} - Bono: {g.get_bono_gerencial()}")

# Mostrar desarrolladores con más de 10 horas extras
print("\nDesarrolladores con más de 10 horas extras:")
for d in Desarrollador.desarrolladores:
    if d.get_horas_extras() > 10:
        print(f"{d.get_nombre()} {d.get_apellido()} - Horas extras: {d.get_horas_extras()}")
