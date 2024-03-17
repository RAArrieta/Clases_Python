# WHILE
# num = 5
# while num != 0:
#     print(num)
#     num -= 1
#     if num == 0:
#         print(f"Llegamos a {num} y sale del while")
        
# while True:
#     print("es un bucle infinito, sali con ctrl+c")

# ****BREAK PERMITE SALIR CUANDO CUMPLIMOS CON ALGO****
# num = 0
# while num < 3:
#     txt= input("Ingrese SI:")
#     if txt == "SI":
#         print("Ingresaste correctamente...") 
#         break
#     num += 1
# else:
#     print("Agotaste tus 3 intentos...")

# ****CONTINUE CORTA DE LEER EL CODIGO Y VUELVE AL PRINCIPIO DE WHILE
i = 0
while i < 10:
    i += 1
    if i == 3 or i==5 or i==7:
        continue
    print(f"i : {i}")

# ****PASS SOLO ES PARA SEÑALAR QUE EN ESA PARTE DEL CODIGO DEBO ESCRIBIR ALGO
# i = 0
# while i < 10:
#     i += 1
#     if i == 3:
#         pass
#         print("tengo el valor de 3")
#     print(f"i : {i}")