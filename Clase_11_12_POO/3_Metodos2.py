class Perro:
    especie = "Mamifero"
    
    def __init__(self, nombre: str, raza: str):    
        self.nombre = nombre
        self.raza = raza
        # puedo crear una variable
        pasos = int(input("Cuantos pasos daremos? "))
        self.caminar(pasos)

    def caminar(self, pasos: int):
        print(f"Con {self.nombre} caminaremos {pasos} pasos")
    

perro1 = Perro("Soos", "Cachulero")