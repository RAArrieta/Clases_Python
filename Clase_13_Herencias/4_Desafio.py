"""
A partir del código anterior, crear una clase Usuario
que herede de la clase Cliente. Tendrá como variable de instancia
contraseña: str  (no será un parámetro del método constructor)
contraseña llamará al método generar_contraseña(), que devolverá un str, 
que consiste en los primeros 4 caracteres de 'nombres' y los úlimos 2 
caracteres de 'telefono'
"""

class Persona:
    def __init__(self, nombres: str, apellidos: str):
        self.nombres = nombres
        self.apellidos = apellidos
    def nombre_completo(self) -> None:
        print(f"{self.apellidos}, {self.nombres}")

class Cliente(Persona):
    def __init__(self, nombres: str, apellidos: str, telefono: str):
        super().__init__(nombres, apellidos)
        self.telefono = telefono

