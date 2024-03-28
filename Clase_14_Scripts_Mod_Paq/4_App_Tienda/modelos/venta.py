# Crear una clase Articulo:
#   - nombre: str
#   - precio: float
#   - __str__()
# Crear clase Pedido:
#   - variable de clase: lista_de_pedidos = []
#   - variables de instancia:
#       - usuario: Usuario
#       - articulo: Articulo
#   - __str__()
from personas import Usuario

class Articulo:
    def __init__(self, nombre, precio) -> None:
        self.nombre = nombre
        self.precio = precio

    def __str__(self) -> str:
        return f"{self.nombre} {self.precio}"

class Pedido:
    lista_de_pedidos = []

    def __init__(self, usuario= Usuario, articulo = Articulo) -> None:
        self.usuario = usuario
        self.articulo = articulo

producto1 = Articulo("Muzzarella",3800)

print(producto1)