from registrar_un_evento import crear_evento , newoplogistico
from eventos_disponibles import eventos_disponibles
from limpiar_consola import limpiar_consola
from comprar_boleta import compraboletas
from verificar_boleta import verificar_boleta
from consultar_boleteria import boletas_compradas

def menuadmin():
    condicion_menu = 1
    while condicion_menu == 1:
        limpiar_consola()
        print("\n\n\t--------Bienvenido De Vuelta A Taquilla Online Usuario Admin!--------")
        print("\n\tQue Desea Hacer El Dia De Hoy?")
        print("\n(1)-Crear Un Evento")
        print("\n(2)-Ver Eventos Creados")
        print("\n(3)-Crear Un Operador Logistico")

        opcion = int(input("\nIngrese el número de la opción deseada (1-3): "))

        if opcion == 1:
            limpiar_consola()
            crear_evento()
            break
        elif opcion == 2:
            limpiar_consola()
            eventos_disponibles() 
            condicion = int(input("Si Deseas Volver Al Inicio Del Menu Presiona (1), De Lo Contrario Para Finalizar Presiona (2): "))
            if condicion == 1:
                condicion_menu = 1
            elif condicion == 2:
                condicion_menu = 0
        elif opcion == 3:
            limpiar_consola()
            newoplogistico()
            break
        else:
            print('----------------------------------------------------------------------')
            print("\tOpción inválida. Por favor, ingrese un número válido.")
            print('----------------------------------------------------------------------')
            
def menuser():
    condicion_menu = 1
    while condicion_menu == 1:
        limpiar_consola()
        print("\n\n\t--------Bienvenido A Taquilla Online Usuario--------")
        print("\n\tQue Desea Hacer El Dia De Hoy?")
        print("\n(1)-Ver Eventos Disponibles Y Comprar Boletas")
        print("\n(2)-Consultar Mis Boletas Compradas")
        
        opcion = int(input("\nIngrese el número de la opción deseada (1-2): "))

        if opcion == 1:
            eventos_disponibles()
            condicion_user = int(input("Si Deseas Comprar Boletas Para El Evento Presiona (1), De Lo Contrario Presiona (2): "))
            if condicion_user == 1: 
                compraboletas() 
            else: 
                limpiar_consola()
                print("\tGracias Por Usar Taquilla Online, Te Esperamos Pronto De Vuelta!")
            break
        elif opcion == 2:
            boletas_compradas()
            condicion = int(input("Si Deseas Volver Al Inicio Del Menu Presiona (1), De Lo Contrario Para Finalizar Presiona (2): "))
            if condicion == 1:
                condicion_menu = 1
            elif condicion == 2:
                condicion_menu = 0
            break
        else:
            print('----------------------------------------------------------------------')
            print("\tOpción inválida. Por favor, ingrese un número válido.")
            print('----------------------------------------------------------------------')
            
            
def menuoplogistico():
    condicion_menu = 1
    while condicion_menu == 1:
        limpiar_consola()
        print("\n\n\t--------Bienvenido A Taquilla Online Operador Logistico--------")
        print("\n\tQue Desea Hacer El Dia De Hoy?")
        print("\n(1)-Validar Legitimidad De La Boleteria")
        
        opcion = int(input("\nIngrese el número de la opción deseada: "))

        if opcion == 1:
            verificar_boleta()
            break
        else:
            limpiar_consola()
            print('----------------------------------------------------------------------')
            print("\tOpción inválida. Por favor, ingrese un número válido.")
            print('----------------------------------------------------------------------')
            condicion_menu = int(input("\nPresiona (1) Para Volver Al Menu O (2) Para Salir Del Programa: "))