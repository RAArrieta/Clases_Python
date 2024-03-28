class Cliente:
    """Clase para crear clientes"""

    def __init__(self, nombre) -> None:
        self.nombre = nombre

    def __str__(self):
        return self.nombre


class Usuario(Cliente):
    """Usuario hereda de Cliente y tiene como atributos
    el email y el password para su login y posterior compra de pedidos"""

    def __init__(self, nombre, email, password) -> None:
        super().__init__(nombre)
        self.email = email
        self.password = password

    def __str__(self):
        return f"{self.nombre} ({self.email})"


if __name__ == "__main__":
    cliente = Cliente("RuizSeñor")
    print(cliente)
    usuario = Usuario("RuizSeñor", "ruiz@email", "passw")
    print(usuario)

# Hacer pruebas unitarias con pytest