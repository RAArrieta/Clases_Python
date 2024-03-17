# LOS PARAMETROS LLEGAN POR POSICION SALVO QUE LE DEMOS NOMBRE
# def resta (b,a,c):
#     return print(c-a-b)

# resta (c=100, b=12, a=15)

# *ARGS CANTIDAD INDEFINIDA DE PARAMETROS
# def suma (*args):
#     i = 0
#     for arg in args:
#         i += arg
#     return print(i)

# suma (5, 6, 3, 8, 10)

# ALTERNATIVA A LO ANTERIOR
# def suma (*args):
#     return sum(args)

# print(suma (5, 6, 3, 8, 10))

# **KWARGS SIRVE PARA KEY Y VALUE
# def test (**kwargs):
#     for clave, valor in kwargs.items():
#         print (f"Clave: {clave}, Valor: {valor}")

# test(a=1,b=2,c=3)

def mostrar (**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

diccionario = {"amarillo": "yellow", "blue": "azul"}
mostrar (**diccionario)
