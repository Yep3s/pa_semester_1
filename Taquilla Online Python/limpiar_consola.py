import os
def limpiar_consola():
    if os.name == 'nt':  # esta funcion la utilizamos para borrar la consola cada que se ejecute el programa dependiendo el sistema operativo
        os.system('cls') #windows
    else: 
        os.system('clear') # Linux/Mac