import pandas as pd
from limpiar_consola import limpiar_consola

def verificar_boleta():
    limpiar_consola()
    print("\n\tBienvenido A La Seccion De Verificacion De Boleteria De Taquilla Online")
    
    while True:
        condicion = int(input("\nSi Deseas Verificar Una Boleta Presiona (1), De Lo Contrario Presiona (2): "))
        
        if condicion == 1:
            limpiar_consola()
            clave = input("Ingrese La Clave De La Boleta A Verificar: ")
            df = pd.read_csv('keys_boleteria.csv')
            boletas_compradas = df[df['Clave'] == clave]['Localidad']
        
            if not boletas_compradas.empty:
                print("\n\tLa Boleta Es Veridica")
                for boleta in boletas_compradas:
                    print(f'\nEsta Es La Localidad De La Boleta: {boleta}')
            else:
                limpiar_consola()
                print("--------------------------------------------------------------------------------------")
                print("\tError: No se Encontraron Boletas Compradas Con La Clave Ingresada.")
                print("--------------------------------------------------------------------------------------")
        elif condicion == 2:
            limpiar_consola()
            print("-----------------------------------------------------------------------------------------------")
            print("\tGracias Por Utilizar El Servicio De Verificacion De Boleteria De Taquilla Online")
            print("-----------------------------------------------------------------------------------------------")
            break
        else:
            limpiar_consola()
            print("--------------------------------------------------------------------------------------")
            print("\tOpción inválida. Por favor, selecciona una opción válida.")
            print("--------------------------------------------------------------------------------------")

