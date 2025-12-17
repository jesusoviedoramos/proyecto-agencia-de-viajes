# Importamos la funcion conectar desde conexion.py y se conecta a la bd
from conexion import conectar

# Contiene todos los paquetes turisticos
class Paquete:

    # Metodo estatico para crear un nuevo paquete turístico
    @staticmethod
    def crear():
        # Se establece la conexión a la base de datos
        conn = conectar()
        cursor = conn.cursor()

        # Se solicitan los datos del paquete al administrador
        nombre = input("Nombre del paquete: ")
        descripcion = input("Descripción: ")

        # El precio se ingresa con puntos 0.000.000 y se eliminan los puntos para guardarlo como numero entero en la bd
        precio_input = input("Precio: ")
        precio = int(precio_input.replace(".", ""))

        cursor.execute(
            "INSERT INTO paquetes (nombre, descripcion, precio) VALUES (%s,%s,%s)",
            (nombre, descripcion, precio)
        )

        # Se guardan los cambios en la base de datos y se cierra el cursor y la conexión
        conn.commit()

        cursor.close()
        conn.close()

        print("Paquete creado correctamente\n")

    # Mostrar todos los paquetes
    @staticmethod
    def mostrar_paquetes():
        conn = conectar()
        cursor = conn.cursor()

        # Consulta sql para obtener todos los paquetes
        cursor.execute("SELECT * FROM paquetes")
        paquetes = cursor.fetchall()

        # Se recorren y muestran los paquetes uno por uno
        for p in paquetes:
            # Se formatea el precio con puntos para mostrarlo al usuario 0.000.000
            precio_formateado = f"{int(p[3]):,}".replace(",", ".")
            print("--------------------------------------")
            print(f"ID: {p[0]}")
            print(f"Nombre: {p[1]}")
            print(f"Descripción: {p[2]}")
            print(f"Precio: ${precio_formateado}")

        print("--------------------------------------\n")

        # Se cierran el cursor y la conexión
        cursor.close()
        conn.close()

    # Editar un paquete existente
    @staticmethod
    def editar():
        conn = conectar()
        cursor = conn.cursor()

        # Se solicita el ID del paquete para modificar
        idd = int(input("ID del paquete a editar: "))

        # Se solicitan los nuevos datos
        nombre = input("Nuevo nombre: ")
        descripcion = input("Nueva descripción: ")
        precio_input = input("Nuevo precio: ")
        precio = int(precio_input.replace(".", ""))

        # Consulta sql para actualizar el paquete
        cursor.execute("""
            UPDATE paquetes
            SET nombre=%s, descripcion=%s, precio=%s
            WHERE id=%s
        """, (nombre, descripcion, precio, idd))

        # Se guardan los cambios y se cierra el cursor y la conexión
        conn.commit()

        cursor.close()
        conn.close()

        print("Paquete actualizado correctamente\n")

    # Eliminar un paquete
    @staticmethod
    def eliminar():
        conn = conectar()
        cursor = conn.cursor()

        # Se solicita el ID del paquete para eliminar
        idd = int(input("ID del paquete a eliminar: "))

        # Consulta sql para eliminar el paquete
        cursor.execute("DELETE FROM paquetes WHERE id=%s", (idd,))

        # Se guardan los cambios y se cierra el cursor y la conexion
        conn.commit()

        cursor.close()
        conn.close()

        print("Paquete eliminado correctamente\n")

