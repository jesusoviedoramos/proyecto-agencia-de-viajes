# Importa la funcion conectar desde el archivo conexion.py y se conecta a la bd
from conexion import conectar

# Importa la libreria bcrypt para encriptar y verificar contraseñas
import bcrypt

# La clase Usuario maneja el registro e inicio de sesión de usuarios
class Usuario:

    # Metodo estatico para registrar usuarios
    @staticmethod
    def registrar():
        conn = conectar()
        cursor = conn.cursor()

        # Menu para elegir el tipo de cuenta
        print("\n--- REGISTRAR USUARIO ---")
        print("1. Usuario")
        print("2. Administrador")

        # Se pide el tipo de cuenta
        tipo = input("Tipo de cuenta: ")

        # Se solicitan las credenciales
        username = input("Nombre de usuario: ")
        password = input("Contraseña: ")

        # Si el usuario quiere crear una cuenta de administrador
        if tipo == "2":
            # Se pide un código secreto para administradores para mayor seguridad
            codigo = input("Ingrese código de administrador: ")

            # Se valida el codigo
            if codigo != "JJG":
                print("Código incorrecto, no se puede crear administrador.\n")
                cursor.close()
                conn.close()
                return

            # Si el codigo es correcto, se creara la cuenta con el rol de administrador
            rol = "admin"
        else:
            # Si no es administrador, se crea un usuario normal
            rol = "user"

        # Se encripta la contraseña usando bcrypt
        password_hash = bcrypt.hashpw(
            password.encode("utf-8"),  # Convierte la contraseña a bytes
            bcrypt.gensalt()            # Genera un salt aleatorio
        )

        try:
            # Se inserta el usuario con la contraseña ya hasheada en la base de datos
            cursor.execute(
                "INSERT INTO usuarios (username, password_hash, rol) VALUES (%s,%s,%s)",
                (username, password_hash, rol)
            )
            conn.commit()  # Guarda los cambios en la base de datos
            print(f"Cuenta {rol} creada correctamente.\n")

        except Exception as e:
            # Manejo de errores por ejemplo usuario duplicado
            print("Error al crear usuario:", e)

        finally:
            # Se cierra el cursor y la conexión
            cursor.close()
            conn.close()

    # Metodo estatico
    @staticmethod
    def login():
        # Se establece conexión con la base de datos
        conn = conectar()
        cursor = conn.cursor()

        # Se piden las credenciales
        username = input("Nombre de usuario: ")
        password = input("Contraseña: ")

        # Se busca el usuario en la base de datos
        cursor.execute(
            "SELECT id, password_hash, rol FROM usuarios WHERE username=%s",
            (username,)
        )
        user = cursor.fetchone()

        # Se cierra el cursor y la conexion
        cursor.close()
        conn.close()

        # Si el usuario no existe se notifica
        if not user:
            print("Usuario no encontrado.\n")
            return None, None

        # Se obtienen los datos del usuario
        id_usuario, password_hash, rol = user

        # Se verifica la contraseña ingresada con la almacenada
        if bcrypt.checkpw(password.encode("utf-8"), password_hash):
            print(f"Bienvenido {username} ({rol})\n")
            return id_usuario, rol
        else: 
            print("Contraseña incorrecta.\n")
            return None, None
