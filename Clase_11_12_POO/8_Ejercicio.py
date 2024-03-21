"""
A partir del código de 6_Ejercicio2.py (clase Producto),
crear el método especial __str__ que muestre:
     <nombre>: $<precio>
"""

class Producto:
    def __init__(self, nombre: str, precio: float) -> None:
        self.nombre = nombre
        self.precio = precio
        
    def modificar_precio (self):
        self.precio = float(input(f"Ingrese el nuevo precio de {self.nombre}\n>> "))
        
    def __str__(self) -> str:
        mostrar = f"{self.nombre} cuesta: ${self.precio:.2f}"
        return mostrar
    
producto1 = Producto("Muzzarella", 3200)
producto2 = Producto("Lomito", 4500)

print(producto1)
print(producto2)

producto1.modificar_precio()
producto2.modificar_precio() 

print("NUEVOS PRECIOS")
print(producto1)
print(producto2)