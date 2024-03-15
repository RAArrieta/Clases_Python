# num = 5
# while num != 0:
#     print(num)
#     num -= 1
#     if num == 0:
#         print(f"Llegamos a {num} y sale del while")
        
# while True:
#     print("es un bucle infinito, sali con ctrl+c")

num = 0
while num < 3:
    txt= input("Ingrese SI:")
    if txt == "SI":
        print("Ingresaste correctamente...") 
        break
    num += 1
else:
    print("Agotaste tus 3 intentos...")
