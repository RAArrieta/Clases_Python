tupla = (8, 15, 4, 39, 5, 89, 87, 19, 7, -755, 88, 123, 2, 11, 15, 9, 355)

print (tupla)

print(f"El ultimo item es {tupla[-1:]}")
print(f"Tiene {len(tupla)} items")
print(f"El nro 87 se encuentra en la posicion {tupla.index(87)}")
print(f"Formo una lista con los 3 ultimos {list(tupla[-3:])}")
print(f"Valor en la posición 8: {tupla[8]}")
print(f"El nro 7 esta {tupla.count(7)} veces")

