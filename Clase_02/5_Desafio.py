lista_1 = [0, 1, 2, 3, 4, 5]
lista_2 = ["string", True, False, 234, 23.34]

# 1
lista_1.append(456789)
lista_1.append("Hola mundo")

print(lista_1)

# 2
lista_2.append("Hola y Adios")
lista_2.append(5555)

print(lista_2)

# 3
lista_3 = lista_1[0:len(lista_1)-1:1]
print(lista_3)

# 4
lista_4 = lista_2[1:len(lista_2)-1:1]
print(lista_4)

# 5
lista_5 = lista_4 + lista_3
print(lista_5)