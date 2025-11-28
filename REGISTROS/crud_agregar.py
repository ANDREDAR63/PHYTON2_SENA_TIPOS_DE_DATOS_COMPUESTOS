# crud_agregar.py
import csv
# No necesita importar Usuario, solo necesita usar su método a_lista()

def agregar_usuario(nombre_archivo, usuario):
    """Agrega un nuevo usuario al archivo CSV."""
    try:
        # Abrir en modo 'a' para añadir al final
        with open(nombre_archivo, 'a', newline='') as f:
            escritor = csv.writer(f)
            escritor.writerow(usuario.a_lista()) 
        print(f"\n✅ Usuario con ID {usuario.id} agregado con éxito.")
    except Exception as e:
        print(f"\n❌ Error al agregar el usuario: {e}")