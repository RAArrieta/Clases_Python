class Producto:
    def __init__(self, nombre: str, precio: float) -> None:
        self.nombre = nombre
        self.precio = precio
        
    def __str__(self) -> str:
        mostrar = f"{self.nombre} cuesta ${self.precio:.2f}"
        return mostrar
        
producto1 = Producto("Muzzarella", 3800)

# Al string lo llamo directamente con el nombre del objeto
print(producto1)

# A su vez puedo seguir llamandolo por sus atributos
print(producto1.nombre)
print(producto1.precio)