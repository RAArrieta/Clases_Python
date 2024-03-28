# Crear una clase Cliente con el atributo "nombre"
# Crear una clase Usuario que herede de Cliente
# Usuario tendrá 2 atributos: email y password
# Crear una clase Articulo:
#   - nombre: str
#   - precio: float
#   - __str__()
# Crear clase Pedido:
#   - variable de clase: lista_de_pedidos = []
#   - variables de instancia:
#       - usuario: Usuario
#       - articulo: Articulo
#   - __str__()

from modelos.personas import Usuario  # el primer script ejecutado usa IMPORTACIONES ABSOLUTAS
from modelos.venta import Articulo, Pedido  # el primer script ejecutado usa IMPORTACIONES ABSOLUTAS

esteban = Usuario(nombre="Esteban Acevedo", email="este@correo", password="pass123")
cintia = Usuario(nombre="Cintia Roxana", email="cint@correo", password="pass7894")

print(esteban)
print(cintia)

pan = Articulo(nombre="pan", precio=900)
leche = Articulo(nombre="leche", precio=1500)

print(pan)
print(leche)

pedido_1 = Pedido(esteban, pan)
pedido_2 = Pedido(esteban, leche)
pedido_3 = Pedido(cintia, pan)

print(pedido_1)
print(pedido_2)
print(pedido_3)
print(Pedido.lista_de_pedidos)
print(__name__)