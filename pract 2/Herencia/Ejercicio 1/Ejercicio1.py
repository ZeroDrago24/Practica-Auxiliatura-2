class Vehiculo:
    def __init__(self, marca, modelo, año, precio_base):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.precio_base = precio_base

    def mostrar_info(self):
        return f"El vehiculo con la marca {self.marca}, modelo {self.modelo}, año {self.año}, precio base {self.precio_base}"

class Coche(Vehiculo):
    def __init__(self, marca, modelo, año, precio_base, num_puertas, tipo_combustible):
        super().__init__(marca, modelo, año, precio_base)
        self.num_puertas = num_puertas
        self.tipo_combustible = tipo_combustible

    def mostrar_info(self):
        return f"El coche con la marca {self.marca}, modelo {self.modelo}, año {self.año}, precio base {self.precio_base}, número de puertas {self.num_puertas}, tipo de combustible {self.tipo_combustible}"

class Moto(Vehiculo):
    def __init__(self, marca, modelo, año, precio_base, cilindrada, tipo_motor):
        super().__init__(marca, modelo, año, precio_base)
        self.cilindrada = cilindrada
        self.tipo_motor = tipo_motor

    def mostrar_info(self):
        return f"La moto con la marca {self.marca}, modelo {self.modelo}, año {self.año}, precio base {self.precio_base}, cilindrada {self.cilindrada}, tipo de motor {self.tipo_motor}"


coche1 = Coche("Toyota", "Corolla", 2020, 20000, 4, "Gasolina")
moto1 = Moto("Yamaha", "YZF-R3", 2022, 6000, "321cc", "4 tiempos")

print(moto1.mostrar_info())
print(coche1.mostrar_info())
