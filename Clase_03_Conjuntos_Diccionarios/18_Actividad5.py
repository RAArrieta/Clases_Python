persona = {}
nombre = input("Ingrese su nombre: \n>> ")
persona["nombre"] = nombre
edad = int(input("Ingrese su edad: \n>> "))
persona["edad"] = edad
direccion = input("Ingrese su dirección: \n>> ")
persona["direccion"] = direccion

print(persona)

for clave, valor in persona.items():
    print(f"{clave}: {valor}")

# print(f"{nombre} tiene {edad} años y vive en {direccion}")



