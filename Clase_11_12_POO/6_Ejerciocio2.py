"""
- Crear una clase Producto. 
- Contiene 2 variables de instancia: 
    nombre:str, precio:float
- Contiene 1 método de instancia:
    modificar_precio()
- Crear 2 instancias de la clase Producto
- Imprimir los atributos (o variables) de cada uno
- Modificar el precio de cada instancia (enviar el porcentaje) y mostrarlo
"""

class Producto:
    def __init__(self, nombre: str, precio: float) -> None:
        self.nombre = nombre
        self.precio = precio
        
    def modificar_precio (self):
        self.precio = float(input(f"Ingrese el nuevo precio de {self.nombre}\n>> "))
    
producto1 = Producto("Muzzarella", 3200)
producto2 = Producto("Lomito", 4500)

print(f"{producto1.nombre} cuesta ${producto1.precio:.2f}")
print(f"{producto2.nombre} cuesta ${producto2.precio:.2f}")

producto1.modificar_precio()
producto2.modificar_precio() 

print("NUEVOS PRECIOS")
print(f"{producto1.nombre} cuesta ${producto1.precio:.2f}")
print(f"{producto2.nombre} cuesta ${producto2.precio:.2f}")