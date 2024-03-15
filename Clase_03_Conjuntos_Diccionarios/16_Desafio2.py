campeones_mundiales = {"1990":"Alemania", "1994":"Brasil", "1998":"Francia", "2002":"Brasil", "2006":"Italia", "2010":"España", "2014":"Alemania", "2018":"Francia"}

for clave, valor in campeones_mundiales.items():
    print(f"Año: {clave}, Campeón: {valor}")
    
campeones_mundiales["2022"] = "Argentina"

print("\nACTUALIZAMOS LOS CAMPEONES")

for clave, valor in campeones_mundiales.items():
    print(f"Año: {clave}, Campeón: {valor}")