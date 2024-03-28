class Cliente:
    def __init__(self, nombre) -> None:
        self.nombre = nombre

    def __str__(self) -> str:
        return f"Nombre de cliente {self.nombre}"
    
class Usuario(Cliente):
    def __init__(self, nombre, email, password) -> None:
        self.email = email
        self.password = password
        super().__init__(nombre)
    
    def __str__(self) -> str:
        return f"{self.nombre} {self.email} {self.password}"

usuario = Usuario("Jose", "sdf@sdf", "1234")

print(usuario)