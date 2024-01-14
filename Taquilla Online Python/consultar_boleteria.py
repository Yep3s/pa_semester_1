import pandas as pd

def boletas_compradas():
    # Lee el archivo CSV
    df = pd.read_csv('keys_boleteria.csv')

    # Verifica si el usuario tiene tiquetes comprados
    if df.empty:
        print("No tienes tiquetes comprados.")
    else:
        print("-----------------------------")
        print("Tus Boletas Compradas Son:")
        print("-----------------------------")
        print(df)
        print("-----------------------------")
# Llama a la función para mostrar los tiquetes comprados

