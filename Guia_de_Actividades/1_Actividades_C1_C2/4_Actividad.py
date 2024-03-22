"""
Crea un programa que, teniendo en cuenta la siguiente tupla, 
muestre el valor del segundo elemento de la misma. 
Además, debe mostrar cuántas veces se repite este valor y cuál es el índice del valor repetido.

Ten en cuenta que la primera aparición sería la posición 1 de la tupla, por lo cual deberíamos buscar el índice de la siguiente aparición.
"""

palabras_tupla = (
    "manzana", 
    "pera", 
    "uva", 
    "naranja", 
    "sandía", 
    "manzana", 
    "plátano", 
    "kiwi", 
    "pera", 
    "fresa", 
    "mango", 
    "uva", 
    "cereza", 
    "manzana", 
    "durazno"
    )

segundo_elemento = palabras_tupla[1]
print(segundo_elemento)

cantidad_repetidas = palabras_tupla.count(segundo_elemento)
print(f"{segundo_elemento} esta {cantidad_repetidas} veces en la tupla")

index_pera = palabras_tupla.index("pera")
print(f"la segunda vez que aparece '{segundo_elemento}' es en el indice {palabras_tupla.index("pera", index_pera+1)}")


