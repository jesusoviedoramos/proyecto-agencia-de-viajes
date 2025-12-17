# Importa la función conectar desde el archivo conexion.py y esto conecta a la bd
from conexion import conectar

# Esta clase maneja todas las operaciones CRUD de la tabla destinos
class Destino:

    # Metodo estatico para CREAR un nuevo destino
    # No se necesita crear un objeto Destino para usarse
    @staticmethod
    def crear():
        conn = conectar()

        # Se crea un cursor para ejecutar consultas SQL
        cursor = conn.cursor()

        # Se solicitan los datos del destino
        nombre = input("Nombre del destino: ")
        descripcion = input("Descripción: ")
        actividades = input("Actividades disponibles: ")

        # Se pide el costo como texto para permitir puntos como separador de miles 0.000.000 o 0000000
        costo_input = input("Costo: ")

        # Se eliminan los puntos y se convierte el costo a entero 
        costo = int(costo_input.replace(".", ""))

        # Consulta SQL para insertar un nuevo destino en la tabla destinos
        cursor.execute(
            "INSERT INTO destinos (nombre, descripcion, actividades, costo) VALUES (%s,%s,%s,%s)",
            (nombre, descripcion, actividades, costo)
        )

        # Se confirman los cambios en la base de datos y se cierra el cursor y la conexión
        conn.commit()

        cursor.close()
        conn.close()

        print("Destino creado correctamente\n")

    # Metodo estataico para MOSTRAR todos los destinos
    @staticmethod
    def mostrar():
        # Se establece la conexion y se crea el cursor
        conn = conectar()

        cursor = conn.cursor()

        # Consulta SQL para obtener todos los registros de la tabla destinos
        cursor.execute("SELECT * FROM destinos")

        # Se obtienen todos los resultados de la consulta
        destinos = cursor.fetchall()

        # Se recorren los destinos uno por uno
        for d in destinos:
            # Se formatea el costo con separador de miles
            costo_formateado = f"{int(d[4]):,}".replace(",", ".")

            # Se muestran los datos del destino
            print("--------------------------------------")
            print(f"ID: {d[0]}")
            print(f"Nombre: {d[1]}")
            print(f"Descripción: {d[2]}")
            print(f"Actividades: {d[3]}")
            print(f"Costo: ${costo_formateado}")

        print("--------------------------------------\n")

        # Se cierra el cursor y la conexión
        cursor.close()
        conn.close()

    # Método estático para EDITAR un destino existente
    @staticmethod
    def editar():

        # Se establece la conexión
        conn = conectar()
        
        # Se crea el cursor
        cursor = conn.cursor()
        
        # Se solicita el ID del destino que se desea modificar
        idd = int(input("ID del destino a editar: "))
        
        # Se solicitan los nuevos datos
        nombre = input("Nuevo nombre: ")
        descripcion = input("Nueva descripción: ")
        actividades = input("Nuevas actividades: ")
        costo_input = input("Nuevo costo: ")
        
        # Se formatea el costo
        costo = int(costo_input.replace(".", ""))

        # Consulta sql para actualizar el destino según su ID
        cursor.execute("""
            UPDATE destinos
            SET nombre=%s, descripcion=%s, actividades=%s, costo=%s
            WHERE id=%s
        """, (nombre, descripcion, actividades, costo, idd))

        # Se confirman los cambios y se cierran la conexion y el cursor
        conn.commit()

        cursor.close()
        conn.close()

        print("Destino actualizado correctamente\n")

    # Método estático para ELIMINAR un destino
    @staticmethod
    def eliminar():
        # Se establece la conexión
        conn = conectar()

        # Se crea el cursor
        cursor = conn.cursor()

        # Se solicita el ID del destino a eliminar
        idd = int(input("ID del destino a eliminar: "))

        # Consulta SQL para eliminar el destino por ID
        cursor.execute("DELETE FROM destinos WHERE id=%s", (idd,))

        # Se confirman los cambios y se cierra el cursor y la conexión
        conn.commit()

        cursor.close()
        conn.close()

        print("Destino eliminado correctamente\n")
