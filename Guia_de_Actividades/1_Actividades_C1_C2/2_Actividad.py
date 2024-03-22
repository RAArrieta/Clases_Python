"""
Crea un programa que tome una cadena de texto como entrada del usuario.
Luego, muestra por pantalla los primeros tres caracteres de la cadena, 
seguidos por los tres últimos caracteres. 
Además, concatena ambos subconjuntos y muestra el resultado.
"""

cadena = "otorrinolaringologo"

sli1 = cadena[ : 3] 
sli2 = cadena[-3: ]

resultado = sli1 + sli2

print (resultado)