class Vehiculo:
    def __init__(self, modelo: str, potencia: int) -> None:
        self.modelo = modelo 
        self.motor = self.Motor(potencia)
        
    class Motor:
        def __init__(self, potencia) -> None:
            self.potencia = potencia
            
mi_auto = Vehiculo("Sandero", 1600)

print(mi_auto.modelo)
print(mi_auto.motor.potencia)