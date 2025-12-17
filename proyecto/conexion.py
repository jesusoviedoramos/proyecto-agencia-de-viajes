# Importa el modulo mysql.connector que permite conectar python con mysql
import mysql.connector
# Importa error para manejar errores especificos de mysql
from mysql.connector import Error
def conectar():
    try:
        # Se establece la conexion con la base de datos mysql
        conn = mysql.connector.connect(
            host="localhost",        
            database="viajes_aventura",  
            user="root",             
            password="Jeshujechu1?", 
            port="3306",             # Puerto para mysql (3306 es el estandar)
            #connection_timeout=5,    # Tiempo maximo (en segundos) para intentar conectar
            #autocommit=False         # Desactiva el guardado automatico de cambios
            #esas 2 partes del codigo no aplica mucho en este codigo pero se pondria solo por buena plactica, Control de transacciones, Conexión eficiente y Código más profesional 
        )

        # Si la conexion fue exitosa, se devuelve el objeto conexion
        return conn

    except Error as e:
        # Mensaje de error
        print("Error al conectar a la base de datos:", e)

        return None
