import pandas as pd
import os
from limpiar_consola import limpiar_consola
from menus import menuser
limpiar_consola()

def iniciousernormal():
    # Muestra mensaje de bienvenida
    print("\n\tBienvenido A La Seccion De Usuarios De Taquilla Online\n")
    
    usuario = {}  # se crea el diccionario para almacenar los datos del usuario
    
    #le pregunta al usuario si desea crear una cuenta nueva o iniciar sesión
    condicion = int(input("Si desea crear un usuario presione (1), de lo contrario si deseas ingresar con tu cuenta presiona (2): "))
    
    if condicion == 1:
        # pide datos para crear una cuenta nueva
        nombres = input("\nIngresa Tu o Tus Nombres: ")
        usuario['nombres'] = nombres

        apellidos = input("\nIngresa Tu o Tus Apellidos: ")
        usuario['apellidos'] = apellidos

        cedula = int(input("\nIngresa Tu Numero De Cedula: "))
        usuario['cedula'] = cedula

        telefono = int(input("\nIngresa Numero De Telefono: "))
        usuario['telefono'] = telefono

        correo = input("\nIngresa Tu Correo Electronico: ")
        usuario['correo'] = correo

        # Valida la contraseña
        while True:
            password = input("\nCrea Una Contraseña Para Tu Cuenta De Taquilla Online: ")
            usuario['password'] = password
            password_2 = input("\nConfirma La Contraseña: ")        
            if password == password_2:
                print('----------------------------------------------------------------------')
                print("\t\tContraseña Guardada Exitosamente")
                print('----------------------------------------------------------------------')
                break
            else:
                print("\n\tError: Las Contraseñas No Concuerdan.")
        
        # Muestra los datos ingresados por el usuario
        print('----------------------------------------------------------------------')
        print("\n\tLos Datos Registrados Para La Creacion De El Usuario Fueron:")
        print("\nNombre/s Y Apellido/s Del Usuario: " + usuario['nombres'] + " " +  usuario['apellidos'])
        print("\nCedula Del Usuario: " + str(usuario['cedula']) )
        print("\nTelefono Del Usuario: " + str(usuario['telefono']) )
        print("\nCorreo Del Usuario: " + usuario['correo'] )
        print("\nLa Contraseña Ingresada Por El Usuario Fue: " + usuario['password'])
        
        # Crear un DataFrame con los datos del usuario
        df = pd.DataFrame.from_dict(usuario, orient='index', columns=['valor']).transpose()
        ruta_datos = 'user_data.csv'
        
        # Guardar los datos del usuario en un archivo CSV
        df.to_csv(ruta_datos, index=False, columns=['nombres', 'apellidos', 'cedula', 'telefono','correo','password'])
        
        print('----------------------------------------------------------------------')
        print("\t\tUsuario Registrado Con Exito")
        print('----------------------------------------------------------------------')
    
    elif condicion == 2:
        if not os.path.isfile('user_data.csv'):
            print("\n\tError: No Hay Ningun Usuario Encontrado En La Base De Datos")
            print("\n\t------Debes Crear Un Usuario Para Poder Acceder A Taquilla Online------")
        else:
            #verifica las credenciales del usuario
            def verificar_credenciales(correo, password):
                datos = pd.read_csv('user_data.csv')
                filtro = (datos['correo'] == correo) & (datos['password'] == password)
                return filtro.any()
            
            while True:
                correo = input("\nIngresa Tu Correo Electrónico: ")
                password = input("\nIngresa La Contraseña De Tu Cuenta De Taquilla Online: ")
                
                if verificar_credenciales(correo, password):
                    print("\n\t¡Bienvenido De Vuelta A Taquilla Online, Usuario!")
                    menuser()
                    break
                else:
                    print("\n\tError: Las Credenciales Ingresadas No Concuerdan.")
    else:
        print("\n\tError: La Opcion Ingresada No Es Validad")
