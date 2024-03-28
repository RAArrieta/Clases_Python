from .persona import Cliente

def ingresar_cliente():
    nombre = input("Nombre: ")
    telefono = int(input("Teléfono: "))
    direccion = input("Dirección: ")
    cliente1 = Cliente(nombre, telefono, direccion)
    return cliente1