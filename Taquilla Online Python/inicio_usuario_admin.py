from limpiar_consola import limpiar_consola
limpiar_consola()

#Usuario De Prueba: 
#correo: susana999@gmail.com - contraseña: tomate - usuario admin
                        

def iniciouseradmin():
    print("\n\tBienvenido A La Seccion De Administradores De Taquilla Online")
    while True:
        correo = input("\nIngresa Tu Correo Electronico: ") #pide que ingrese el correo
        password = input("\nIngresa La Contraseña De Tu Cuenta De Taquilla Online: ") #pide que ingrese la contraseña
        if correo == "susana999@gmail.com" and password == "tomate": #si los datos ingresados sonn iguales a los de aqui finaliza el codigo
            break
        else:
            print("\n\tError: Las Credenciales Ingresadas No Concuerdan.") #si los datos son diferentes emite este error

