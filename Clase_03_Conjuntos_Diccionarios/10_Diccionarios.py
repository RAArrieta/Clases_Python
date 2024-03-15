# LOS DICCIONARIOS TIENEN CLAVE Y VALOR, VAN ENTRE {}

diccionario_vacio = {}

print(type(diccionario_vacio))

diccionario = {"amarillo": "yellow", "blue": "azul"}

print(diccionario)
print(diccionario["amarillo"])

# SON MUTABLES

diccionario["amarillo"] = "hielou"
print(f"El nuevo valor es {diccionario['amarillo']}")

# TAMBIEN SE PUEDEN HACER OPERACIONES

numeros = {"edad": 5, "edad2": 13}
numeros["edad"] += 10

print(f"Le agrego 10 a edad: {numeros['edad']}")