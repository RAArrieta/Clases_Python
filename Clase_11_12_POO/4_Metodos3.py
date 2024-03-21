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
        
    def presentacion (self) -> str:
        presentacion = f"{self.nombre} es un {self.raza}"
        return presentacion

perro1 = Perro("Soos", "Cachulero")
# print(perro1.presentacion())

# TIP para ver la variable y su valor
print(f"{perro1.nombre=}")