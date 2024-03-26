# CUANDO HAY DOS CLASES Y UNA (HIJA) PUEDE HEREDAR LOS ATRIBUTOS Y METODOS DEL PADRE

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
    pass

soos = Perro("Mamifero", 1)

print(soos.especie)
print(soos.edad)
soos.describirme()
