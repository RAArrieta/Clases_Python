# SON LO MISMO QUE LAS LISTAS PERO ESTAS NO SE PUEDEN MODIFICAR, VAN ENTRE ()
# SE PUEDE USAR FUNCIONES LEN, COUNT E INDEX

variable = 321
variable_2 =[1, 2]
tupla = (1, True, "Hola", 4, 5.2, variable, variable_2)

# SI HACEMOS UNA TUPLA CON UN UNICO VALOR ES ASI
tupla_2 =(6,)

print (tupla)
# print(tupla[2])
# print(tupla[-1])

# SI ME PERMITE MODIFICAR UNA LISTA POR INDICE
variable_2[1] = 123
print(tupla)

print(tupla[0:4])