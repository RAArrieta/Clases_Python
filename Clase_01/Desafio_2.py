PARTIDO_GANADO = 3
PARTIDO_EMPATADO = 1
PARTIDO_PERDIDO = 0

partido_ganado = int(input("Cantidad de partidos ganados:\n>> "))
partido_empatado = int(input("Cantidad de partidos empatados:\n>> "))
partido_perdido = int(input("Cantidad de partidos perdidos:\n>> "))

puntos_totales = PARTIDO_GANADO * partido_ganado + PARTIDO_EMPATADO * partido_empatado
cantidad_de_partidos = partido_ganado + partido_empatado + partido_perdido

promedio = puntos_totales / cantidad_de_partidos

print (f"Ya que se jugaron {cantidad_de_partidos} partidos y consiguieron {puntos_totales} puntos, el promedio es de {round(promedio,2)} puntos por partido.-")