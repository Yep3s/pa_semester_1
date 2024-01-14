import pandas as pd
from datetime import date
from limpiar_consola import limpiar_consola

def eventos_disponibles():
    limpiar_consola()
    
    # Leer el archivo CSV
    datos_evento = pd.read_csv('datos_evento.csv')
    
    # Obtener la fecha actual
    fecha_actual = date.today()
    fecha_actual_enformato = fecha_actual.strftime("%d/%m/%Y")
    
    print('-----------------------------------------------------------------------------------------------------------')

    # Imprime la fecha actual
    print(f'\tLos Eventos Creados Y Disponibles A La Fecha De Hoy {fecha_actual_enformato}, Son: ')
    
    # Extraer detalles del primer evento
    nombre_evento = datos_evento.loc[0, 'nombre_del_evento']
    capacidad_evento = datos_evento.loc[0, 'capacidad_del_evento']
    num_localidades = datos_evento.loc[0, 'numero_de_localidades']
    descripcion_evento = datos_evento.loc[0, 'descripcion_del_evento']
    fecha_evento = datos_evento.loc[0, 'fecha_del_evento']
    
    # Imprimir información del evento
    print('-----------------------------------------------------------------------------------------------------------')
    print(f"\n-Nombre del evento: {nombre_evento}")
    print(f"\n-Capacidad del evento: {capacidad_evento} Personas")
    print(f"\n-Numero de localidades: {num_localidades}")
    print(f"\nDescripcion del evento: {descripcion_evento}")
    print(f"\nFecha Del Evento: {fecha_evento}")
    print('-----------------------------------------------------------------------------------------------------------')
