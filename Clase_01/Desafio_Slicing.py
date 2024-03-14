cadena = "acitametaM , 5.8 , otipeP ordeP"

# 1
cadena_volteada = cadena [::-1]
print (cadena_volteada)

# 2
# nombre_alumno = cadena_volteada [0:12:1]
nombre_alumno = cadena [-1:-13:-1]
print (nombre_alumno)

#3
nota = cadena_volteada [15:18:1]
print (nota)

#4
materia = cadena_volteada [21::1]
print (materia)

print (f"{nombre_alumno} a sacado un {nota} en {materia}.")
