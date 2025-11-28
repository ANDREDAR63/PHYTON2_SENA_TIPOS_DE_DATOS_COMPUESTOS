# inicializador.py
import csv
from utilidades_csv import ENCABEZADOS

def inicializar_archivo(nombre_archivo):
    """Asegura que el archivo CSV exista y tenga los encabezados."""
    try:
        with open(nombre_archivo, 'r', newline='') as f:
            lector = csv.reader(f)
            try:
                next(lector) 
            except StopIteration:
                pass 
    except FileNotFoundError:
         with open(nombre_archivo, 'w', newline='') as f:
             escritor = csv.writer(f)
             escritor.writerow(ENCABEZADOS)