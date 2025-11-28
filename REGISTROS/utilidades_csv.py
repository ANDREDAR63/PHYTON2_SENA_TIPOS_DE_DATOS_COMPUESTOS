# utilidades_csv.py
import csv

ENCABEZADOS = ['id', 'nombre', 'apellido', 'edad', 'estado_civil']

def leer_todas_las_filas(nombre_archivo):
    """Lee todas las filas de datos (excluyendo el encabezado) y retorna una lista de listas."""
    filas = []
    try:
        with open(nombre_archivo, 'r', newline='') as f:
            lector = csv.reader(f)
            next(lector)  # Saltar el encabezado
            for fila in lector:
                if fila:
                    filas.append(fila)
        return filas
    except FileNotFoundError:
        print("Error: El archivo de datos no fue encontrado.")
        return []

def escribir_todas_las_filas(nombre_archivo, filas):
    """Reescribe todo el archivo con los encabezados y las filas proporcionadas."""
    with open(nombre_archivo, 'w', newline='') as f:
        escritor = csv.writer(f)
        escritor.writerow(ENCABEZADOS)
        escritor.writerows(filas)