# crud_leer.py
from usuarios import Usuario
from utilidades_csv import leer_todas_las_filas

def ver_usuarios(nombre_archivo):
    """Lee y retorna una lista de objetos Usuario de todas las filas."""
    filas = leer_todas_las_filas(nombre_archivo)
    usuarios = []
    for fila in filas:
        try:
            usuarios.append(Usuario(*fila)) 
        except (ValueError, IndexError) as e:
            print(f"⚠️ Fila inválida omitida: {fila}. Error: {e}")
            
    return usuarios