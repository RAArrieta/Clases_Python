class Producto:
    def __init__(self, nombre: str, precio: float) -> None:
        self.nombre = nombre
        self.precio = precio
        
    def __str__(self) -> str:
        mostrar = f"{self.nombre}: ${self.precio:.2f}"
        return mostrar
    
    def __repr__(self) -> str:
        return f"Producto({self.nombre}, {self.precio:.2f})"

class Pedido:
    lista_de_pedidos: list[Producto] = []
    
    def __init__(self) -> None:
        self.pedido: list[Producto] = []
        
    def agregar_producto(self, *args: Producto):
        for producto in args:
            self.pedido.append(producto)
            Pedido.lista_de_pedidos.append(producto)

producto1 = Producto("Muzzarella", 3500)
producto2 = Producto("Especial", 4200)
producto3 = Producto("Napolitana", 4000)
producto4 = Producto("Calabresa", 4200)

sancho = Pedido()
quijote = Pedido()

sancho.agregar_producto(producto1, producto2)
quijote.agregar_producto(producto3, producto4)

print(Pedido.lista_de_pedidos)
print(sancho.pedido)
print(quijote.pedido)