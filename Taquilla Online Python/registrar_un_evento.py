import pandas as pd
import os
from limpiar_consola import limpiar_consola
    
limpiar_consola()     

def crear_evento():
    datos_evento = {}  #SE CREA EL DICCIONARIO DATOS_EVENTO, DONDE SE ALMACENARAN TODOS LOS DATOS INGRESDADOS POR EL USUARIO

    print("\n\tBienvenido A La Seccion De Creacion De Evento De Taquilla Online")
    # Crear Evento - (nombre - capacidad max)
    nombre_del_evento = input('\n-Ingresa el nombre del evento: ') #EL USUARIO INGRESA EL NOMBRE DEL EVENTO
    datos_evento['nombre_del_evento'] = nombre_del_evento #CREA LA LLAVE 'NOMBRE_DEL_EVENTO' Y EL VALOR DE ESTA LLAVE SERA EL INGRESADO ANTERIOR MENTE POR EL USUARIO
    
    while True:
        try:
            capacidad_del_evento = int(input('\n-Ingresa la capacidad maxima de personas para el evento: ')) #EL USUARIO INGRESA la capacidad maxima de personas para el evento
            datos_evento['capacidad_del_evento'] = capacidad_del_evento #CREA LA LLAVE 'capacidad_del_evento' Y EL VALOR DE ESTA LLAVE SERA EL INGRESADO ANTERIOR MENTE POR EL USUARIO
            break
        except ValueError: #VALUE ERROR ES UN TIPO DE ERROR QUE YA ESTA DEFINIDO EN PYTHON Y AL DETECTAR ESTE ERROR LANZARA LA EXCEPTION
            print("\n\tError: Debes ingresar un número entero.")
    
    # Crear Numero De Localidades 
    while True:
        try:
            numero_de_localidades = int(input('\n-Ingresa el número de localidades que desea crear para este evento: ')) #EL USUARIO INGRESA el número de localidades que desea crear para el evento
            datos_evento['numero_de_localidades'] = numero_de_localidades #CREA LA LLAVE 'numero_de_localidades' Y EL VALOR DE ESTA LLAVE SERA EL INGRESADO ANTERIOR MENTE POR EL USUARIO
            break
        except ValueError: #VALUE ERROR ES UN TIPO DE ERROR QUE YA ESTA DEFINIDO EN PYTHON Y AL DETECTAR ESTE ERROR LANZARA LA EXCEPTION
            print("\n\tError: Debes ingresar un número entero.")
        
    localidades = {} #SE CREA EL DICCIONARIO localidades, DONDE SE ALMACENARAN LOS NOMBRES DE LAS LOCALIDADES INGRESADAS POR EL USUARIO Y SUS RESPECTIVOS VALORES POR ESPACIOS
    
    capacidad_max = [capacidad_del_evento] #SE CREA LA LISTA capacidad_max, DONDE SE HARAN OPERACIONES PARA DEFINIR LA CAPACIDAD MAXIMA DE ESPACIOS POR LOCALIDAD 
    
    for x in range(numero_de_localidades): #CREAMOS UN CICLO FOR QUE ITERA DEPENDIENDO EL VALOR INGRESADO EN NUMERO DE LOCALIDADES
        # Crear Localidades - #Accedemos al ultimo elemento de la lista con [-1]
        capacidad_disponible = capacidad_max[-1]
        for d in localidades.values(): #ITERAMOS los valores de localidades 
            capacidad_disponible -= d['num_espacios'] #luego restamos a capacidad dsiponible la iteracion de d y se crea la llave numero de espacios cuyo valor sera la iteracion de d
        localidad = {} #SE CREA EL DICCIONARIO localidad, donde ingresaremos el nombre de la localidad y 
        nombre_localidad = input("\n-Ingrese el nombre de la localidad "+str(x+1)+": ") #CREA LA LLAVE 'nombre_localidad' Y EL VALOR DE ESTA LLAVE SERA EL INGRESADO por el usuario
        localidad['nombre_localidad'] = nombre_localidad
        localidad['valor_localidad'] = int(input(f"\n-Ingrese el Valor para la localidad {nombre_localidad}: "))
        localidad['num_espacios'] = 0   #CREA LA LLAVE 'num_espacios' Y EL VALOR DE ESTA LLAVE sera igual a 0

        while True:
            try:
                num_espacios = int(input(f'\n-Ingrese el número de espacios por localidad (capacidad disponible: {capacidad_disponible}): ')) #se ingresa el numero de espacios por localidad
                if num_espacios <= capacidad_disponible: #si el numero de espacios es menor o igual a la capacidad_disponible (sigue leyendo abajo)
                    localidad['num_espacios'] = num_espacios #trae la llave 'num_espacios' y le asigna el valor ingresado  por el usuario
                    break
                else:
                    print("\n\tError: El número ingresado es mayor al máximo disponible.\n")  
            except ValueError:
                print("\n\tError: Debes ingresar un número entero.\n")
        
        localidades['localidad_'+str(x+1)] = localidad 
    
    datos_evento['localidades'] = localidades 
    
    descripcion_del_evento = input('\n-Ingresa la descripción del evento: ')
    datos_evento['descripcion_del_evento'] = descripcion_del_evento
    
    fecha_del_evento = input('\n-Ingrese la fecha del evento en el siguiente formato (d/m/a): ')
    datos_evento['fecha_del_evento'] = fecha_del_evento
    
    def datosevento():
        limpiar_consola()
        print('-----------------------------------------------------')
        print("\n\tLos Datos Registrados Para El Evento Son:")
        print("\n-Nombre del evento: " + datos_evento['nombre_del_evento'])
        print("\n-Capacidad del evento: " + str(datos_evento['capacidad_del_evento']) + " Personas")
        print("\n-Numero de localidades: " + str(datos_evento['numero_de_localidades']) )
        print("\n\tLocalidades, Precios Y Espacios:")
        for localidad_num, localidad_data in datos_evento['localidades'].items():
            nombre_localidad = localidad_data['nombre_localidad']
            valor_localidad = localidad_data['valor_localidad']
            espacios_localidad = localidad_data['num_espacios']
            print(f"\n-Localidad : {nombre_localidad} - Precio: {valor_localidad} - Numero De Espacios: {espacios_localidad}")
        print("\nDescripcion del evento: " + datos_evento['descripcion_del_evento'])
        print("\nFecha Del Evento: " + datos_evento['fecha_del_evento'])
    
        print('-----------------------------------------------------')
    datosevento()
        
    while True:
        try:
            decision_2 = int(input("Si Los Datos Ingresados Son Correctos Presiona (1) Para Crear El Evento, De Lo Contrario Presiona (2): "))
            if decision_2 == 1:
                print("\n\tEl Registro Del Evento Ha Sido Exitoso!")
                break
            else:
                print("Que Datos Necesitas Corregir?: ")
        except ValueError:
            print("\n\tError: Debes ingresar un número entero.\n") 
                
    df = pd.DataFrame.from_dict(datos_evento, orient='index', columns=['valor']).transpose()
    # selecciona la ruta
    ruta = "datos_evento.csv"
    ruta_localidades = "datos_localidades.csv"
    # Guardar el DataFrame en un archivo CSV en la ruta especificada
    df.to_csv(ruta, index=False, columns=['nombre_del_evento', 'capacidad_del_evento', 'numero_de_localidades', 'descripcion_del_evento', 'fecha_del_evento'])

    for localidad_num, localidad_data in datos_evento['localidades'].items():
        df_2 = pd.DataFrame.from_dict(localidad_data, orient='index', columns=['valor']).transpose()
        if not os.path.isfile(ruta_localidades):
            df_2.to_csv(ruta_localidades, index=False, mode='w')
        else:
            df_2.to_csv(ruta_localidades, index=False, mode='a', header=False)    
                   
def newoplogistico():
    print("\n\tBienvenido A La Seccion De Creacion De Operadores Logisticos De Taquilla Online\n")
    usuario = {}
    condicion = int(input("Si desea crear un usuario presione (1), de lo contrario si deseas salir del programa presiona (2): "))
    
    if condicion == 1:
            nombres = input("\nIngresa El Nombre Del Operador Logistico: ")
            usuario['nombres'] = nombres
    
            apellidos = input("\nIngresa El Apellido Del Operador Logistico: ")
            usuario['apellidos'] = apellidos

            cedula = int(input("\nIngresa El Numero De Cedula Del Operador Logistico: "))
            usuario['cedula'] = cedula
        
            telefono = int(input("\nIngresa El Numero De Telefono Del Operador Logistico: "))
            usuario['telefono'] = telefono
    
            correo = input("\nIngresa El Correo Electronico Del Operador Logistico: ")
            usuario['correo'] = correo
            
            while True:
                    password = input("\nCrea Una Contraseña Para La Cuenta Del Operador Logistico: ")
                    usuario['password'] = password
                    password_2 = input("\nConfirma La Contraseña: ")        
                    if password == password_2:
                        print('----------------------------------------------------------------------')
                        print("\t\tContraseña Guardada Exitosamente")
                        print('----------------------------------------------------------------------')
                        break
                    else:
                        (print("\n\tError: Las Contraseñas No Concuerdan."))
            print('----------------------------------------------------------------------')
            print("\n\tLos Datos Registrados Para La Creacion De El Usuario Fueron:")
            print("\nNombre/s Y Apellido/s Del Usuario: " + usuario['nombres'] + " " +  usuario['apellidos'])
            print("\nCedula Del Usuario: " + str(usuario['cedula']) )
            print("\nTelefono Del Usuario: " + str(usuario['telefono']) )
            print("\nCorreo Del Usuario: " + usuario['correo'] )
            print("\nLa Contraseña Ingresada Por El Usuario Fue: " + usuario['password'])
            
            df = pd.DataFrame.from_dict(usuario, orient='index', columns=['valor']).transpose()
            ruta_datos = 'user_oplogistico.csv'
            df.to_csv(ruta_datos, index=False, columns=['nombres', 'apellidos', 'cedula', 'telefono','correo','password'])
            
            print('----------------------------------------------------------------------')
            print("\t\tUsuario Registrado Con Exito")
            print('----------------------------------------------------------------------')
            
    elif condicion == 2:
        print("\n\tGracias Por Usar Taquilla Online, Te Esperamos De Vuelta Pronto!")
    else:
        print("\n\tError: La Opcion Ingresada No Es Validad")
        
        