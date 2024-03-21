class Producto:
    def __init__(self, nombre: str, precio: float) -> None:
        self.nombre = nombre
        self.precio = precio
            
    def __str__(self) -> str:
        mostrar = f"{self.nombre} cuesta: ${self.precio:.2f}"
        return mostrar
    
    def __repr__(self) -> str:
        return f"Producto(nombre:'{self.nombre}', precio:{self.precio:.2f})"
    
producto1 = Producto("Muzzarella", 3200)
producto2 = Producto("Lomito", 4500)

# print(producto1)
# print(producto2)

# La idea es que el programador vea mejor la info del objeto 
print(repr(producto1))
print(repr(producto2))

