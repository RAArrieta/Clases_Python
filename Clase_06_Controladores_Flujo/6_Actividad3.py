nombre = input("Como es tu nombre?\n>> ")
preferencia = input("Cual prefieres C o M?\n>> ")

nombre1= nombre.strip().lower()[0]
preferencia1 = preferencia.strip().lower()[0]

if preferencia1 == "c" or preferencia1 == "m":
    if preferencia1 == "m" and nombre1 <= "m": print("Perteneces al grupo A")
    elif preferencia1 == "c" and nombre1 >= "n": print("Perteneces al grupo A")
    else: print("Perteneces al grupo B")
else:
    print("Ingrese correctamente su preferencia...")