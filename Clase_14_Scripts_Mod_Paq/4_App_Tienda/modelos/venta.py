# from typing import Self
from .personas import Usuario  # las importaciones entre módulos de un paquete usan IMPORTACIONES RELATIVAS

# es decir, se usa el punto


class Articulo:
    """Son productos con un nombre y un precio"""

    def __init__(self, nombre, precio) -> None:
        self.nombre = nombre
        self.precio = precio

    def __str__(self) -> str:
        return f"{self.nombre}: ${self.precio:.2f}"


class Pedido:
    """Consiste en un usuario que compra un artículo
    y se guarda en una lista de pedidos"""

    lista_de_pedidos: list["Pedido"] = []
    # lista_de_pedidos: list[Self] = []

    def __init__(self, usuario: Usuario, articulo: Articulo) -> None:
        self.usuario = usuario
        self.articulo = articulo
        Pedido.lista_de_pedidos.append(self)

    def __str__(self) -> str:
        return f"- - - {self.usuario} compró: {self.articulo}"

    def __repr__(self) -> str:
        return f"{self.usuario} compró: {self.articulo}"