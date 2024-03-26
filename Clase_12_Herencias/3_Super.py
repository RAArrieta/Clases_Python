# SUPER NOS PERMITE ACCEDER A METODOS DEL PADRE DESDE LA HIJA
# SI QUIERO AGREGAR UN ATRIBUTO A UN METODO TENGO DOS OPCIONES

class Animal():
    def __init__(self, especie, edad) -> None:
        self.especie = especie
        self.edad = edad
        
    def hablar(self):
        pass
    
    def moverse(self):
        pass
    
    def describirme (self):
        print(f"Soy un {type(self).__name__}")

class Perro(Animal):
    # FORMA 1
    def __init__(self, especie, edad, dueño) -> None:
    #     self.especie = especie
    #     self.edad = edad
    #     self.dueño = dueño
        
        # FORMA 2
        super().__init__(especie, edad)
        self.dueño = dueño
        
    def hablar(self):
        print("Guau")
    def moverse(self):
        print("Camino en 4 patas")
        
soos = Perro("Mamifero", 1, "Alfredo")

print(soos.especie)
print(soos.edad)
print(soos.dueño)