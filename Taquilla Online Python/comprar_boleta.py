import pandas as pd
import random
import string
import os
from limpiar_consola import limpiar_consola

def compraboletas():
    limpiar_consola()

    # Leer el archivo CSV de localidades
    df_localidades = pd.read_csv('datos_localidades.csv')

    # Obtener las localidades disponibles
    localidades_disponibles = df_localidades['nombre_localidad'].unique()

    # Obtener los precios por localidad
    precios_localidades = df_localidades[['nombre_localidad', 'valor_localidad']].drop_duplicates()

    print("\n\tBienvenido A La Seccion De Compra De Boleteria De Taquilla Online")

    # Cargar el archivo CSV existente en un DataFrame, si existe
    archivo_existente = 'keys_boleteria.csv'
    if os.path.exists(archivo_existente):
        df_boletas_existente = pd.read_csv(archivo_existente)
    else:
        df_boletas_existente = pd.DataFrame()

    # Crear un diccionario para almacenar el contador de boletas por localidad
    contador_boletas = {}

    # Inicializar la condición de compra
    condicion = 1

    while condicion == 1:
        # Mostrar los precios por localidad al usuario
        print("\nLas Localidades Disponibles Y Sus Precios Son:")
        for _, row in precios_localidades.iterrows():
            print(f"\nLocalidad: {row['nombre_localidad']} - Precio: {row['valor_localidad']}")

        # Solicitar al usuario el tipo de localidad
        tipo_localidad = input(
            "\nIngrese El Nombre De La Localidad Que Desea Comprar, De Lo Contrario Presiona (2) Para Finalizar: ")

        # Verificar si se desea finalizar la compra
        if tipo_localidad.lower() == "2":
            break

        # Verificar si la localidad ingresada es válida
        if tipo_localidad not in localidades_disponibles:
            print("Localidad no encontrada.")
            continue

        # Obtener el precio de la localidad seleccionada
        precio_localidad = df_localidades.loc[
            df_localidades['nombre_localidad'] == tipo_localidad, 'valor_localidad'].values[0]

        # Obtener el contador actual de boletas para la localidad
        if tipo_localidad in contador_boletas:
            contador_actual = contador_boletas[tipo_localidad]
        else:
            contador_actual = 1

        # Solicitar al usuario la cantidad de boletas
        cantidad_boletas = int(
            input(
                f"\nIngrese la cantidad de boletas que desea comprar (Disponibles {df_localidades.loc[df_localidades['nombre_localidad'] == tipo_localidad, 'num_espacios'].values[0]}): "))

        # Verificar si hay suficientes espacios disponibles en la localidad seleccionada
        cantidad_disponible = df_localidades.loc[df_localidades['nombre_localidad'] == tipo_localidad,'num_espacios'].values[0]
        if cantidad_boletas > cantidad_disponible:
            print("No hay suficientes espacios disponibles en la localidad seleccionada.")
            continue

        # Actualizar la cantidad de espacios disponibles en el DataFrame
        df_localidades.loc[df_localidades['nombre_localidad'] == tipo_localidad, 'num_espacios'] -= cantidad_boletas

        # Generar las claves de las boletas y crear el DataFrame de boletas compradas
        claves = [''.join(random.choices(string.ascii_uppercase + string.digits, k=4)) for _ in range(cantidad_boletas)]
        localidad = [f"{tipo_localidad}_{contador_actual + i}" for i in range(cantidad_boletas)]
        boletas_localidad = pd.DataFrame({'Localidad': localidad, 'Clave': claves})

        # Actualizar el contador de boletas para la localidad
        contador_boletas[tipo_localidad] = contador_actual + cantidad_boletas

        # Verificar si ya existen boletas para esta localidad
        if not df_boletas_existente.empty:
            if tipo_localidad in df_boletas_existente['Localidad'].unique():
                # Concatenar las nuevas boletas con las existentes
                df_boletas_existente = pd.concat([df_boletas_existente, boletas_localidad])
            else:
                # Agregar las nuevas boletas al DataFrame existente
                df_boletas_existente = pd.concat([df_boletas_existente, boletas_localidad])
        else:
            # El DataFrame existente está vacío, usar solo las nuevas boletas
            df_boletas_existente = boletas_localidad

        # Verificar si se ha agregado alguna boleta al carrito
        if len(boletas_localidad) > 0:
            # Calcular el valor total a pagar
            total_pagar = len(boletas_localidad) * precio_localidad

            # Mostrar el resumen del carrito y el total a pagar
            limpiar_consola()
            print("\n\t\t\tResumen de la compra")
            print(f'\n\t\t-Numero De Boletas: {cantidad_boletas}')
            print(f'\n\t\t-Localidad De Las Boletas: {tipo_localidad}')
            print(f"\n\t\tEl Total A Pagar Es De: ${total_pagar}")

            # Solicitar confirmación de la compra
            confirmacion = input("\nPara Confirmar La Compra Presiona (1), De Lo Contrario Presiona (2): ")

            # Verificar la confirmación de la compra
            if confirmacion.lower() == '1':
                # Guardar los cambios en el archivo de localidades
                df_localidades.to_csv('datos_localidades.csv', index=False)

                # Guardar el DataFrame de boletas en el archivo CSV existente
                df_boletas_existente.to_csv(archivo_existente, index=False)

                limpiar_consola()
                print('-----------------------------------------------------')
                print("\t\t¡Compra exitosa!")
                print('-----------------------------------------------------')

                condicion = int(input("\nSi Desea Seguir Comprando Boletas Presione (1), De Lo Contrario Presiona (2): "))
                limpiar_consola()
                if condicion == 2:
                    print('---------------------------------------------------------------')
                    print("\tGracias Por Comprar En Taquilla Online, Vuelve Pronto!")
                    print('---------------------------------------------------------------')
            else:
                limpiar_consola()
                print('-----------------------------------------------------')
                print("\t\tCompra cancelada.")
                print('-----------------------------------------------------')
        else:
            print("No se han agregado boletas al carrito.")
