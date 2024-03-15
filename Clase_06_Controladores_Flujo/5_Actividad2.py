edad = 18
antiguedad = 5
ingreso = 4000

if edad >= 18:
    if antiguedad >= 3 and ingreso >= 2500:
        print("Ud puede acceder al prestamo") 
    elif antiguedad < 3 and ingreso >= 4000:
        print("Ud puede acceder al prestamo") 
    elif antiguedad < 3:
        print("Por no tener la antiguedad requerida ud debe cobrar para acceder al prestamo $4000")
else:
    print("Debe ser mayor de 18 para acceder al credito...")
    