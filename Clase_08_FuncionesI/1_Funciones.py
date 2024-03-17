

# DEF CON EL CREO LA FUNCION, PUEDO PASARLE UN PARAMETRO
# def saludar(nombre):
#     print(f"Hola {nombre}!!")

# nombre = input("Cual es tu nombre?\n>> ")

# saludar(nombre)

# RETURN ESPECIFICO QUE DEVUELVO DE LA FUNCION
def saludar(nombre):
    respuesta = print(f"Hola {nombre}!!")
    return respuesta

nombre = input("Cual es tu nombre?\n>> ")

saludar(nombre)