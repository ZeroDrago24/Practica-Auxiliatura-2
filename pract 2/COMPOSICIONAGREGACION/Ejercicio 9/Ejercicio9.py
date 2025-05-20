class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def mostrar_info(self):
        print(f"Producto: {self.nombre}, Precio: Bs {self.precio}")

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_precio(self):
        return self.precio

    def set_precio(self, precio):
        self.precio = precio


class CarritoCompras:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        if len(self.productos) < 10:
            self.productos.append(producto)
            print(f"Producto '{producto.get_nombre()}' agregado al carrito.")
        else:
            print("¡Carrito lleno! No se pueden agregar más de 10 productos.")

    def mostrar_carrito(self):
        print("\nCarrito de Compras:")
        if not self.productos:
            print("El carrito está vacío.")
        else:
            for producto in self.productos:
                producto.mostrar_info()

    def get_productos(self):
        return self.productos


# Crear productos
p1 = Producto("Leche", 8)
p2 = Producto("Pan", 2)
p3 = Producto("Arroz", 12)
p4 = Producto("Queso", 25)

# Crear carrito
carrito = CarritoCompras()

# Agregar productos al carrito
carrito.agregar_producto(p1)
carrito.agregar_producto(p2)
carrito.agregar_producto(p3)
carrito.agregar_producto(p4)

# Intentar agregar más de 10 para probar límite
for i in range(7):
    carrito.agregar_producto(Producto(f"Producto{i+5}", 10))

# Este debería fallar al ser el producto 11
carrito.agregar_producto(Producto("ProductoExtra", 50))

# Mostrar información del carrito
carrito.mostrar_carrito()
