"""
Crea una clase llamada "Círculo" que represente un círculo. 
La clase debe tener un atributo de clase llamado "pi" 
con un valor constante de 3.14159. 
Además, la clase debe tener un atributo de instancia "radio" 
que se recibe como argumento en el constructor.
La clase "Círculo" debe tener un método llamado 
"calcular_area" que calcule y devuelva el área del círculo 
utilizando la fórmula: area = pi * radio ^ 2.

Escribe el código de la clase "Círculo" 
a) crea una instancia de la misma. 
b) Luego, accede al atributo de clase "pi" 
c) y utiliza el método "calcular_area" para obtener y mostrar el área del círculo.
"""
import math

class Circulo:
    PI=math.pi
    def __init__(self, radio: float) -> None:
        self.radio = radio
        
    def calcular_area(self):
        area = Circulo.PI * self.radio ** 2
        return area
        
circulo = Circulo(float(input("Cuanto mide el radio de tu circulo?\n>> ")))


print(f"El area de tu circulo es de {round(circulo.calcular_area(),2)}")