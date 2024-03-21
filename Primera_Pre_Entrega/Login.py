base_de_datos = []

def menu ():
    while True:
        print("=============")
        print("*** LOGIN ***")
        print("=============\n")
        print("1 - Crear usuario")
        print("2 - Ingresar")
        print("3 - Modificar mis datos")
        print("4 - Ver Clientes ingresados")
        print("5 - Salir")
        opcion = int(input("\nOpción: "))
        if opcion >= 1 and opcion <= 5:
            if opcion == 1:
                cargar_usuario()
            elif opcion == 2:
                if len(base_de_datos)!=0:
                    ingresar()
                else:
                    print("\nPrimero debe cargar clientes...")
            elif opcion == 3:
                if len(base_de_datos)!=0:
                    modificar_usuario()
                else:
                    print("\nPrimero debe cargar clientes...")
            elif opcion == 4:
                if len(base_de_datos)!=0:
                    ver_usuarios()
                else:
                    print("\nPrimero debe cargar clientes...")
            elif opcion == 5:
                print("Hasta pronto")
                exit()
        else:
            print("Ingreso un valor incorrecto...")
            
def cargar_usuario():
    print("=============")
    print("NUEVO USUARIO")
    print("=============")
    nombre = input("Ingrese su nombre de Usuario\n>> ")
    contrasena = input("Ingrese su contraseña\n>> ")
    base_de_datos.append({"Nombre": nombre, "Contraseña": contrasena})
           
def ingresar ():
    x = 1
    print("=======")
    print("INGRESO")
    print("=======")
    nombre = input("Ingrese su Usuario\n>> ")
    contrasena = input("Ingrese su Contraseña\n>> ")
    for usuario in base_de_datos:
        print("Entre a for")
        x += 1
        if nombre == usuario["Nombre"] and contrasena == usuario["Contraseña"]:
            print("El cliente existe...")
            break
        elif x == len(usuario):
            print("El cliente no existe...")
   
def modificar_usuario():
    print("=================")
    print("MODIFICAR USUARIO")
    print("=================")
    while True:
        nombre = input("Ingrese su nombre de Usuario\n>> ")
        x = 0
        encontrado = False
        for  x , usuario in enumerate(base_de_datos):
            if usuario["Nombre"] == nombre:
                contrasena = input("Ingrese su nueva contraseña\n>> ")
                base_de_datos[x]["Contraseña"] = contrasena
                print("Se ha modificado su contraseña...")
                encontrado = True
                break        
        if encontrado:
            break
        else:
            print("El usuario no existe...")

def ver_usuarios():
    print("\n===============")
    print("** CLIENTES **")
    print("===============\n")
    for usuario in base_de_datos:
        print(f'Nombre: {usuario["Nombre"]}, Contraseña: {usuario["Contraseña"]}')

def main ():
    menu()
    main()

main ()
