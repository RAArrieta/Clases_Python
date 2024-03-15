cadena = "HoLa MunDo"

# UPPER PARA TODAS MAYUSCULAS
print(f"upper: {cadena.upper()}")

# LOWER PARA TODAS MINUSCULAS
print(f"lower: {cadena.lower()}")

# CAPITALIZE PARA LA PRIMERA EN MAYUSCULA Y EL RESTO EN MINUSCULA
print(f"capitalize: {cadena.capitalize()}")

# TITLE LA PRIMERA DE CADA PALABRA MAYUSCULA Y EL RESTO EN MINUSCULA
print(f"title: {cadena.title()}")

cadena_2 = "Hola amigo como estas amigo"

# COUNT CUENTA TANTO UN CARACTER COMO UNA PALABRA
print(f"count: {cadena_2.count("a")}")
print(f"count: {cadena_2.count("amigo")}")

# FIND ENCUENTRA EN QUE POSICION ESTA UNA PALABRA LA PRIMERA VEZ QUE APARECE
print(f"find: {cadena_2.find("amigo")}")

# RFIND ENCUENTRA EN QUE POSICION ESTA UNA PALABRA LA ULTIMA VEZ QUE APARECE
print(f"rfind: {cadena_2.rfind("amigo")}")

# SPLIT CONVIERTE LA CADENA EN LISTA
print(f"split: {cadena_2.split()}")

# JOIN SEPARA CADA CARACTER CON LO QUE SE INDIQUE
print(f"join: {"*".join(cadena_2)}")

# STRIP ELIMINA AL PRINCIPIO Y AL FINAL DE LA CADENA (SIEMPRE INDICANDO QUE)
cadena_3 = "   Alfredo Arrieta   "
print(f"strip: {cadena_3.strip(" ")}")

# REPLACE CAMBIA UN CARACTER INDICADO POR OTRO 
print(f"replace: {cadena_2.replace("o","O")}")



