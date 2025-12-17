# Importamos las clases principales del sistema
from usuario import Usuario
from paquete import Paquete
from reserva import Reserva
from destino import Destino

# Menu del administrador
def menu_admin():
    while True:
        # Menu principal
        print("\n--- MENÚ ADMINISTRADOR ---")
        print("1. Gestionar paquetes")
        print("2. Gestionar destinos")
        print("3. Salir")

        op = input("Opción: ")

        # Gestion de paquetes turisticos
        if op == "1":
            while True:
                print("\n--- PAQUETES ---")
                print("1. Crear paquete")
                print("2. Ver paquetes")
                print("3. Editar paquete")
                print("4. Eliminar paquete")
                print("5. Volver")

                op_p = input("Opción: ")

                if op_p == "1":
                    Paquete.crear()
                elif op_p == "2":
                    Paquete.mostrar_paquetes()
                elif op_p == "3":
                    Paquete.editar()
                elif op_p == "4":
                    Paquete.eliminar()
                elif op_p == "5": # Se devuelve al menu anterior
                    break
                else:
                    print("Opción no válida")
        # Gestión de destinos
        elif op == "2":
            while True:
                print("\n--- DESTINOS ---")
                print("1. Crear destino")
                print("2. Ver destinos")
                print("3. Editar destino")
                print("4. Eliminar destino")
                print("5. Volver")

                op_d = input("Opción: ")

                if op_d == "1":
                    Destino.crear()
                elif op_d == "2":
                    Destino.mostrar()
                elif op_d == "3":
                    Destino.editar()
                elif op_d == "4":
                    Destino.eliminar()
                elif op_d == "5": #Se devuelve al menu anterior
                    break
                else:
                    print("Opción no válida")

        # Salir del menu administrador
        elif op == "3":
            break
        else:
            print("Opción no válida")


# Menu del usuario
def menu_usuario(id_usuario):
    while True:
        print("\n--- MENÚ USUARIO ---")
        print("1. Ver paquetes")
        print("2. Reservar paquete")
        print("3. Ver mis reservas")
        print("4. Cancelar reserva")
        print("5. Salir")

        op = input("Opción: ")

        if op == "1":
            Paquete.mostrar_paquetes()
        elif op == "2":
            Reserva.crear(id_usuario)
        elif op == "3":
            Reserva.ver_reservas(id_usuario)
        elif op == "4":
            Reserva.cancelar(id_usuario)
        elif op == "5":
            break
        else:
            print("Opción no válida")


# Menu principal para iniciar sesion y registrarse
def main():
    while True:
        print("\n=== VIAJES AVENTURA ===")
        print("1. Iniciar sesión")
        print("2. Registrarse")
        print("3. Salir")

        op = input("Opción: ")

        if op == "1":
            # Iniciar sesion dependiendo el rol
            id_usuario, rol = Usuario.login()

            # Segun el rol, se muestra el menu correspondiente
            if rol == "admin":
                menu_admin()
            elif rol == "user":
                menu_usuario(id_usuario)

        elif op == "2":
            # Registro de usuario o administrador
            Usuario.registrar()

        elif op == "3":
            print("Hasta luego")
            break

        else:
            print("Opción no válida")

if __name__ == "__main__":
    main()
# Esta estructura permite que el programa principal se ejecute únicamente cuando el archivo es ejecutado directamente, 
# evitando ejecuciones involuntarias cuando se importa como módulo