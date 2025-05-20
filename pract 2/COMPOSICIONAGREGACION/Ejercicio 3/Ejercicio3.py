class Parte:
    def __init__(self,nombre,peso):
        self.nombre=nombre
        self.peso=peso
    def mostrar_info(self):
        return f"{self.nombre} {self.peso} kg"
    
class Avion:
    def __init__(self,modelo,fabricante):
        self.partes=[]
        self.modelo=modelo
        self.fabricante=fabricante
    def agregarParte(self,nombre,peso):
        parte=Parte(nombre,peso)
        self.partes.append(parte)
    def mostrar(self):
        print(f"El avion {self.modelo} {self.fabricante}")
        print(f"con las partes: ")
        for i in range(len(self.partes)):
            print(self.partes[i].mostrar_info())

av=Avion("BEBE","Ovama")
av.agregarParte("Motor","1000 T")
av.mostrar()