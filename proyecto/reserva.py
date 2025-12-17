# Importa la funcion conectar desde conexion.py y ase a conexion a la bd
from conexion import conectar

# La clase Reserva contiene todas las funciones relacionadas con las reservas
class Reserva:

    @staticmethod
    def crear(id_usuario):
        conn = conectar()
        cursor = conn.cursor()

        # Se solicita al usuario el ID del paquete que el desea reservar
        id_paquete = int(input("Ingrese ID del paquete a reservar: "))

        # Se consulta el paquete seleccionado para verificar que exista
        cursor.execute(
            "SELECT nombre, precio FROM paquetes WHERE id=%s",
            (id_paquete,)
        )
        paquete = cursor.fetchone()

        # Si no existe el paquete, se cancela la operación
        if not paquete:
            print("ID de paquete no válido\n")
            cursor.close()
            conn.close()
            return

        # Se obtienen el nombre y precio del paquete
        nombre, precio = paquete

        # Se formatea el precio con puntos para mejor visualización 0.000.000
        precio_formateado = f"{int(precio):,}".replace(",", ".")

        # Se muestra al usuario la información del paquete seleccionado
        print("\nPaquete seleccionado:")
        print(f"Nombre: {nombre}")
        print(f"Precio: ${precio_formateado}")

        # Se pide confirmación antes de realizar la reserva
        confirmar = input(
            f"\n¿Está seguro/a de reservar este paquete por un total de ${precio_formateado}? (s/n): "
        ).lower()

        # Si el usuario no confirma, se cancela la reserva
        if confirmar != "s":
            print("Reserva cancelada\n")
            cursor.close()
            conn.close()
            return

        # Se inserta la reserva en la bd
        cursor.execute(
            "INSERT INTO reservas (id_usuario, id_paquete) VALUES (%s,%s)",
            (id_usuario, id_paquete)
        )

        # Se guardan los cambios en la bd y se cierra el cursor y la conexion
        conn.commit()

        cursor.close()
        conn.close()

        print("Reserva realizada correctamente\n")

    # Metodo para mostrar todas las reservas del usuario
    @staticmethod
    def ver_reservas(id_usuario):
        conn = conectar()
        cursor = conn.cursor()

        # Consulta que obtiene las reservas del usuario junto con los datos del paquete
        cursor.execute("""
            SELECT r.id, p.nombre, p.precio
            FROM reservas r
            JOIN paquetes p ON r.id_paquete = p.id
            WHERE r.id_usuario = %s
        """, (id_usuario,))

        reservas = cursor.fetchall()

        # Si el usuario no tiene reservas, se informa
        if not reservas:
            print("No tienes reservas\n")
            cursor.close()
            conn.close()
            return

        # Se muestran las reservas encontradas
        print("\n--- MIS RESERVAS ---")
        for r in reservas:
            precio_formateado = f"{int(r[2]):,}".replace(",", ".")
            print("--------------------------------------")
            print(f"ID Reserva: {r[0]}")
            print(f"Paquete: {r[1]}")
            print(f"Precio: ${precio_formateado}")
        print("--------------------------------------\n")

        # Se cierran cursor y conexión
        cursor.close()
        conn.close()

    # Cancelar una reserva
    @staticmethod
    def cancelar(id_usuario):
        conn = conectar()
        cursor = conn.cursor()

        # Se solicita el ID de la reserva que se desea cancelar
        id_reserva = int(input("Ingrese ID de la reserva a cancelar: "))

        # Se verifica que la reserva pertenezca al usuario
        cursor.execute(
            "SELECT id FROM reservas WHERE id=%s AND id_usuario=%s",
            (id_reserva, id_usuario)
        )

        reserva = cursor.fetchone()

        # Si la reserva no existe o no pertenece al usuario
        if not reserva:
            print("Reserva no encontrada\n")
            cursor.close()
            conn.close()
            return

        # Se solicita confirmación antes de eliminar la reserva
        confirmar = input("¿Está seguro/a de cancelar esta reserva? (s/n): ").lower()

        if confirmar != "s":
            print("Cancelación abortada\n")
            cursor.close()
            conn.close()
            return

        # Se elimina la reserva de la base de datos
        cursor.execute("DELETE FROM reservas WHERE id=%s", (id_reserva,))
        conn.commit()

        # Se cierran cursor y conexión
        cursor.close()
        conn.close()

        print("Reserva cancelada correctamente\n")
