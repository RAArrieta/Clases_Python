# CONJUNTO O SET ES UNA COLECCION DE ELEMENTOS UNICOS, VAN ENTRE {}
# NO PUEDE CONTENER OBJETOS MUTABLES COMO LISTAS, DICCIONARIOS U OTRO CONJUNTO
# NO PODEMOS HACER SLICING CON CONJUNTOS O MANEJARLO POR INDICE

conjunto_1 = {1, 2, 3, 4, 5}
conjunto_2 = {"Hola", "Chau", "?"}
conjunto_vacio = set()

datos = {"hola", True, 321, 55.2, "Chau"}

print (type(datos))

# SI PODEMOS TRANSFORMAR LISTAS A CONJUNTOS Y VICEVERSA

lista = [1, 2, 3]
new_conjuto = set(lista)

print(f"Lista pasado a conjunto: {new_conjuto}")
print(f"Conjunto pasado a lista: {list(new_conjuto)}")

set2 = set(range(10))
print(set2)

# CONVERSION


