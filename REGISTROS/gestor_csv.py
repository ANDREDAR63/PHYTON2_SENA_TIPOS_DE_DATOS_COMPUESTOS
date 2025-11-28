# gestor_csv.py

# gestor_csv.py

from usuarios import Usuario
from inicializador import inicializar_archivo
from crud_agregar import agregar_usuario
from crud_leer import ver_usuarios
from crud_eliminar import eliminar_usuario
from crud_actualizar import actualizar_usuario

class GestorCSV:
    """
    Clase para manejar las operaciones CRUD delegando en módulos externos.
    """
    def __init__(self, nombre_archivo='usuarios.csv'):
        self.nombre_archivo = nombre_archivo
        self.encabezados = ['id', 'nombre', 'apellido', 'edad', 'estado_civil']
        # Llama a la función del módulo inicializador.py
        inicializar_archivo(self.nombre_archivo)

    # Métodos CRUD (Delegación a funciones externas)

    def agregar_usuario(self, usuario):
        """Delega la adición de usuario al módulo crud_agregar."""
        # Se asegura de pasar el nombre del archivo y el objeto usuario (2 argumentos)
        agregar_usuario(self.nombre_archivo, usuario)

    def ver_usuarios(self):
        """Delega la lectura de usuarios al módulo crud_leer."""
        # Solo pasa el nombre del archivo si es necesario por la función externa
        return ver_usuarios(self.nombre_archivo)

    def eliminar_usuario(self, id_usuario):
        """Delega la eliminación de usuario al módulo crud_eliminar."""
        eliminar_usuario(self.nombre_archivo, id_usuario)

    def actualizar_usuario(self, id_usuario, datos_actualizados):
        """Delega la actualización de usuario al módulo crud_actualizar."""
        actualizar_usuario(self.nombre_archivo, id_usuario, datos_actualizados)