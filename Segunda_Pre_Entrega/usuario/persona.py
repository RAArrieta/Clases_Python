class Cliente:
    def __init__(self, nombre: str, telefono: int, direccion: str) -> None:
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion
        
    def __str__(self) -> str:
        return f"**Estoy en str**\nNombre: {self.nombre}\nTeléfono: {self.telefono}\nDirección: {self.direccion}"
        
    def __repr__(self) -> str:
        return f"**Estoy en repr**\nNombre: {self.nombre}\nTeléfono: {self.telefono}\nDirección: {self.direccion}"