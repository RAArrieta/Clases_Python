# LA LISTA ALMACENA TODO TIPO DE VALORES
# VAN ENTRE []

lista_1 = [0, 1, 2, 3, 4, 5]
lista_2 = ["string", True, False, 234, 23.34]
lista_3 = [6, 7, 8, 9, 10]

otra_lista = lista_1 + lista_3

print(otra_lista)

lista_3 += lista_1
lista_3[0]= 77

print( lista_3)



print(lista_2[0], lista_3[-1])