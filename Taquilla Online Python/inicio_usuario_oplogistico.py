from limpiar_consola import limpiar_consola
import pandas as pd
import os
limpiar_consola()

#Usuario De Prueba: 
#correo: susana999@gmail.com - contraseña: tomate - usuario admin
                        

def inicioplogistico():
    # se le da un mensaje de bienvenida
    print("\n\tBienvenido A La Seccion De Operadores Logisticos De Taquilla Online")
    
    if not os.path.isfile('user_oplogistico.csv'):
        print("\n\tError: No Hay Ningun Usuario Encontrado En La Base De Datos")
        print("\n\t------Se Debe Crear Un Usuario Para Poder Acceder A La Seccion De Operadores Logisticos De Taquilla Online------")
    else:
        # verifica las credenciales del operador logístico
        def verificar_credenciales(correo, password):
            datos = pd.read_csv('user_oplogistico.csv')
            filtro = (datos['correo'] == correo) & (datos['password'] == password)
            return filtro.any()
        
        while True:
            correo = input("\nIngresa Tu Correo Electrónico: ")
            password = input("\nIngresa La Contraseña De Tu Cuenta De Taquilla Online: ")
            
            if verificar_credenciales(correo, password):
                print("\n\t¡Bienvenido De Vuelta A Taquilla Online, Operador Logistico!")
                break
            else:
                print("\n\tError: Las Credenciales Ingresadas No Concuerdan.")

