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
    def hablar(self):
        print("Guau")
    def moverse(self):
        print("Camino en 4 patas")
        
class Vaca(Animal):
    def hablar(self):
        print("Muuu")
    def moverse(self):
        print("Camino en 4 patas")
        
class Abeja(Animal):
    def hablar(self):
        print("Bsss")
    def moverse(self):
        print("Vuelo")
        
    def picar(self):
        print("Picarrr")
        
soos = Perro("Mamifero",2)        
lola = Vaca("Mamifero",5)
charly = Abeja("Insecto",1)

print(soos.especie)
soos.describirme()
lola.hablar()
lola.describirme()
charly.picar()
charly.describirme()



