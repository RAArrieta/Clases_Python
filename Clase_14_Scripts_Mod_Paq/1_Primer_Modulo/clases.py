class Alumno:
    def __init__(self, nombre: str, nota: int) -> None:
        self.nombre = nombre
        self.nota = nota
    
    def mostrar_datos(self):
        print(f"Nombre del alumno: {self.nombre}\nNota: {self.nota}")



    