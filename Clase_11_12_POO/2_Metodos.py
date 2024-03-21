class Perro:
    especie = "Mamifero"
    
    def __init__(self, nombre: str, raza: str, velocidad: int):
        print(f"Contruyendo Perro:\n {raza}, {nombre}")
        
        self.nombre = nombre
        self.raza = raza
        self.velocidad = velocidad
    
    # METODOS
    def ladrar(self):
        print("Guau")
    # se pasa el atributo cuando lo llamo
    def caminar(self, pasos):
        print(f"camina {pasos} pasos")
    

perro1 = Perro("Soos", "Cachulero", 10)

# PUEDO LLAMAR A LOS METODOS
perro1.ladrar()
perro1.caminar(15)