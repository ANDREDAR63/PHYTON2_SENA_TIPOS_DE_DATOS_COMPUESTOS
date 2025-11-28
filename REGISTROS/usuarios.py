# usuario.py

class Usuario:
    """
    Representa un usuario con sus atributos básicos.
    """
    # Se utiliza 'id' para coincidir con la clave del diccionario que viene de maestra_de_datos.py
    def __init__(self, id, nombre, apellido, edad, estado_civil): 
        self.id = int(id)
        self.nombre = nombre.upper()
        self.apellido = apellido.upper()
        self.edad = int(edad)
        self.estado_civil = estado_civil.lower()

    def __str__(self):
        return (f"ID: {self.id}, Nombre: {self.nombre} {self.apellido}, "
                f"Edad: {self.edad}, Estado Civil: {self.estado_civil}")
    
    def a_lista(self):
        """Retorna los atributos del usuario como una lista."""
        return [self.id, self.nombre, self.apellido, self.edad, self.estado_civil]