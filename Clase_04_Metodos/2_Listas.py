lista = [1, 2, 3, 4]

# EXTEND AGREGA A LA LISTA VARIOS VALORES
lista += [5, 6, 7]
print(lista)
lista_2 = [8, 9, 10]
lista.extend(lista_2)
print (f"extend: {lista}")

# INSERT AGREGA UN VALOR EN LA LISTA EN UN INDICE ESPECIFICO
lista.insert(3,0)
print (f"insert: {lista}")

# REVERSE INVIERTE LA LISTA
lista.reverse()
print (f"reverse: {lista}")

# SORT ORDENA DE MENOR A MAYOR
lista.sort()
print (f"sort: {lista}")