# maestra_de_datos.py

from gestor_csv import GestorCSV
from usuarios import Usuario

# Inicializa el gestor
gestor = GestorCSV()

def mostrar_menu():
    print("\n" + "="*40)
    print("      Sistema Maestro de Datos CSV")
    print("="*40)
    print("1. Agregar Nuevo Usuario")
    print("2. Ver Todos los Usuarios")
    print("3. Actualizar Usuario por ID")
    print("4. Eliminar Usuario por ID")
    print("5. Salir")
    print("="*40)

def obtener_datos_usuario():
    """Solicita los datos del usuario."""
    while True:
        try:
            # Pide el ID
            id_u = int(input("  Ingrese ID: "))
            break
        except ValueError:
            print("  ❌ ID debe ser un número entero.")
            
    nombre_u = input("  Ingrese Nombre: ").strip()
    apellido_u = input("  Ingrese Apellido: ").strip()
    
    while True:
        try:
            # Pide la Edad
            edad_u = int(input("  Ingrese Edad: "))
            break
        except ValueError:
            print("  ❌ Edad debe ser un número entero.")
            
    estado_c = input("  Ingrese Estado Civil (soltero, casado, etc.): ").strip()
    
    return {
        "id": id_u, # Clave 'id' que coincide con el constructor de Usuario
        "nombre": nombre_u,
        "apellido": apellido_u,
        "edad": edad_u,
        "estado_civil": estado_c
    }

def main():
    """Función principal que ejecuta el bucle del menú."""
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-5): ")

        if opcion == '1':
            print("\n--- ➕ AGREGAR USUARIO ---")
            datos = obtener_datos_usuario()
            try:
                # Usa **datos para pasar el diccionario como argumentos con nombre
                nuevo_usuario = Usuario(**datos) 
                gestor.agregar_usuario(nuevo_usuario)
            except Exception as e:
                # Ahora solo debe capturar errores de I/O o de la clase Usuario
                print(f"❌ Error al crear/agregar el usuario: {e}")

        elif opcion == '2':
            print("\n--- 👁️ LISTA DE USUARIOS ---")
            usuarios = gestor.ver_usuarios()
            if not usuarios:
                print("No hay usuarios registrados.")
            else:
                for user in usuarios:
                    print(user)

        elif opcion == '3':
            print("\n--- 🔄 ACTUALIZAR USUARIO ---")
            try:
                id_a_actualizar = int(input("Ingrese el ID del usuario a actualizar: "))
                print("Ingrese los nuevos datos (deje en blanco para mantener el valor actual):")
                
                nuevos_datos = {}
                
                nuevo_nombre = input("  Nuevo Nombre: ").strip()
                if nuevo_nombre:
                    nuevos_datos['nombre'] = nuevo_nombre
                
                nuevo_apellido = input("  Nuevo Apellido: ").strip()
                if nuevo_apellido:
                    nuevos_datos['apellido'] = nuevo_apellido
                    
                nueva_edad_str = input("  Nueva Edad: ").strip()
                if nueva_edad_str:
                    try:
                        nuevos_datos['edad'] = int(nueva_edad_str)
                    except ValueError:
                        print("  ❌ Edad debe ser un número entero. Se omite la actualización de la edad.")
                        
                nuevo_estado_c = input("  Nuevo Estado Civil: ").strip()
                if nuevo_estado_c:
                    nuevos_datos['estado_civil'] = nuevo_estado_c

                if nuevos_datos:
                    gestor.actualizar_usuario(id_a_actualizar, nuevos_datos)
                else:
                    print("⚠️ No se ingresaron datos para actualizar.")
                    
            except ValueError:
                print("❌ ID debe ser un número entero válido.")

        elif opcion == '4':
            print("\n--- 🗑️ ELIMINAR USUARIO ---")
            try:
                id_a_eliminar = int(input("Ingrese el ID del usuario a eliminar: "))
                gestor.eliminar_usuario(id_a_eliminar)
            except ValueError:
                print("❌ ID debe ser un número entero válido.")

        elif opcion == '5':
            print("\n👋 ¡Gracias por usar el Sistema Maestro de Datos! Saliendo...")
            break

        else:
            print("\n❌ Opción inválida. Por favor, ingrese un número del 1 al 5.")
            
        input("\nPresione ENTER para continuar...")

if __name__ == "__main__":
    main()
    main()