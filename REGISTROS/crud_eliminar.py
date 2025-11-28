# crud_eliminar.py
from utilidades_csv import leer_todas_las_filas, escribir_todas_las_filas

def eliminar_usuario(nombre_archivo, id_usuario):
    """Elimina un usuario por su ID, reescribiendo el archivo."""
    id_a_eliminar = str(id_usuario)
    filas = leer_todas_las_filas(nombre_archivo)
    
    filas_actualizadas = [fila for fila in filas if fila[0] != id_a_eliminar]
    
    if len(filas_actualizadas) == len(filas):
        print(f"\n⚠️ Usuario con ID {id_usuario} no encontrado.")
        return

    escribir_todas_las_filas(nombre_archivo, filas_actualizadas)
    print(f"\n🗑️ Usuario con ID {id_usuario} eliminado con éxito.")