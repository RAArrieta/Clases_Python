class Alumno:
    def __init__(self, nombre: str, nota: int) -> None:
        self.nombre = nombre
        self.nota = nota
        
    def __str__(self) -> str:
        return f"Nombre: {self.nombre}"