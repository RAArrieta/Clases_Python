ano_nacimiento = int(input("En que añon naciste?\n>> "))

if ano_nacimiento >= 1920 and ano_nacimiento <= 1940:
    print("Tu generacion es silenciosa")
elif ano_nacimiento >= 1946 and ano_nacimiento <= 1964:
    print("Eres un Baby Boomer")
elif ano_nacimiento >= 1965 and ano_nacimiento <= 1979:
    print("Perteneces a la generación X")
elif ano_nacimiento >= 1980 and ano_nacimiento <= 2000:
    print("Eres generacion Y")
elif ano_nacimiento >= 2001 and ano_nacimiento <= 2010:
    print("Generacion Z")
else:
    print("No existe generación asociada")