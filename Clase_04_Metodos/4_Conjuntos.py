set1 = {1, 2, 3}

# COPY HACE UNA COPIA DE UN CONJUTO 
set2 = set1.copy()
print(f"copy: {set2}")

set3 = { 3, 4, 5}

# ISDISJOINT COMPARA SI SON DISTINTOS DOS SET, PARA TRUE NINGUN VALOR DEBE SER IGUAL. SI SOLO UNO COINCIDE YA ES FALSE
print(f"isdisjoint: {set1.isdisjoint(set3)}")

# ISSUBSET COMPARA SI SON TOTALMENTE IGUALES
print(f"issubset: {set1.issubset(set2)}")
print(f"issubset: {set1.issubset(set3)}")

# ISSUPERSET COMPRUEBA SI UN SET CONTIENE OTRO
set4 = {1, 2}
print(f"issuperset: {set1.issuperset(set4)}")
print(f"issuperset: {set4.issuperset(set1)}")
print(f"issuperset: {set1.issuperset(set2)}")

# UNION UNE DOS CONJUNTOS SIN REPETIR LOS VALORES
print(f"union: {set1.union(set3)}")

# DIFFERENCE ENCUENTRA LOS VALORES NO COMUNES ENTRE ELLOS
print(f"difference: {set1.difference(set3)}")
print(f"difference: {set3.difference(set1)}")

# DIFFERENCE_UPDATE ENCUENTRA LOS VALORES NO COMUNES Y LOS GUARDA POR LO QUE YA NO QUEDAN REPETIDOS
set1.difference_update(set3)
print(f"difference_update: {set1}")

# INTERSECTION DEVUELVE EL VALOR QUE ESTA EN AMBOS
print(f"intersection: {set2.intersection(set3)}")

# INTERSECTION_UPDATE ENCUENTRA EL VALOR Y LO GUARDA 
set2.intersection_update(set3)
print(f"intersection_update: {set2}")