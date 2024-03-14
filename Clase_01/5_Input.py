nombre = input("Cual es tu nombre?\n>> ")

# EL INPUT SIEMPRE INGRESA EL DATO COMO STRING, HAY QUE PASARLO A ENTERO
edad = int(input("Cuantos años tienes?\n>> "))


print (type(nombre))
print (type(edad))

print (f"Te llamas {nombre} y tienes {edad} años")