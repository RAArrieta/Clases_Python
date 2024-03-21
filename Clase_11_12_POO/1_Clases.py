class Perro:
    # Atributos de clase, estos atribultos son comunes para todos los perros
    especie = "Mamifero"
    
    # Constructor de la clase, cada uno va a tener su nombre y velocidad
    # def __init__(self, nombre, raza, velocidad):
    def __init__(self, nombre: str, raza: str, velocidad: int):
        
        # Atributos de instancia
        self.nombre = nombre
        self.raza = raza
        self.velcidad = velocidad

# de esta manera puedoo llamar a los atributos de clase
print(Perro.especie)

# Asigno los valores de los atributos de instancia
perro1 = Perro("Soos", "Cachulero", 10)
# Los llamo asi
print (f"{perro1.nombre} tiene una velocidad de {perro1.velcidad} Km/h y es un {Perro.especie} {perro1.raza}")    