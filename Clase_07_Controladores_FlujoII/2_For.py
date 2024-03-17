lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
index = 0

# FOR PERMITE ITERAR LAS LISTA LA CANTIDAD QUE YO QUIERA
# for valor in lista:
#     print(f"Valor: {valor}")
#     print(f"Ahora vale {valor*2}")

# PUEDO MODIFICAR LA LISTA
# for valor in lista:
#     lista[index] *= 2
#     index += 1
# print(lista) 

# RANGE
# SOLO CON EL FIN
# for valor in range(5):
#     print(lista[valor])
# CON EL COMIENZO Y EL FIN (EL FIN NO ESTA INCLUIDO)
# for valor in range(2,8):
#     print(lista[valor])
# CON EL ULTIMO INDICO QUE PUEDO DE IR POR EJ DE DOS EN DOS
# for valor in range(0,10,2):
#     print(lista[valor])

# ELSE PARA QUE QUEDE ENTENDIDO QUE ES LO MUESTRA EL RESULTADO
# for valor in lista:
#     lista[index] *= 2
#     index += 1
# else:
#     print(lista) 

# **** SE PUEDE USAR TANTO CONTINUE COMO BREAK
for valor in range(10):
    if lista[valor] == 5:
        continue
    if lista[valor] == 8:
        break
    print(lista[valor])    
else:
    print("termine de iterar...")

