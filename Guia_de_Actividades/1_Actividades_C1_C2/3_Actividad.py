"""
Crea un programa que inicie con una lista de números enteros. 
Luego, solicita al usuario un número entero 
y un índice para reemplazar un elemento en la lista por el nuevo número ingresado en el índice ingresado. 
Imprime la lista resultante.
"""

lista = [1, 2, 3, 4, 5, 6]

numero = int(input("Ingrese un nro entero: "))
index = int(input("Ingrese el index a modificar: "))

while True:
    if index >= 0 and index < len(lista):
        lista[index] = numero
        print(lista)
        break
    else:
        print("Ingreso un index inexistente...")
        print (f"El largo de la lista es {len(lista)}")
        index = int(input("Ingrese otro valor de index: "))