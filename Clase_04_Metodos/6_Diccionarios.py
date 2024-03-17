diccionario = {"amarillo": "yellow", "blue": "azul", "rojo": "red"}

# GET BUSCA UN ELEMENTO A PARTIR DE SU KEY
print(f'get: {diccionario.get("amarillo")}')
print(f'get: {diccionario.get("gray","No existe...")} muestra el segundo si no lo encuentra')

# KEYS MUESTRA TODOS LOS KEY DE UN DICCIONARIO
print(f"keys: {diccionario.keys()}")

# VALUES MUESTRA TODOS LOS VALORES DE UN DICCIONARIO
print(f"values: {diccionario.values()}")

# ITEMS CREA UNA LISTA DE KEY Y VALOR
print(f"items: {diccionario.items()}")

for clave, valor in diccionario.items():
    print(f"Clave: {clave}, Valor: {valor}")
