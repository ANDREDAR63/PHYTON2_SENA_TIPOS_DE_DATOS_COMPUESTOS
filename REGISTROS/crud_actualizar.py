# crud_actualizar.py
from usuarios import Usuario
from utilidades_csv import leer_todas_las_filas, escribir_todas_las_filas

def actualizar_usuario(nombre_archivo, id_usuario, datos_actualizados):
    """Actualiza los datos de un usuario por su ID."""
    id_a_actualizar = str(id_usuario)
    filas = leer_todas_las_filas(nombre_archivo)
    encontrado = False

    for i, fila in enumerate(filas):
        if fila[0] == id_a_actualizar:
            encontrado = True
            
            # Reutilizar el objeto Usuario para mantener la limpieza de datos
            usuario_existente = Usuario(*fila)

            # Aplicar las actualizaciones o mantener el valor existente
            nuevo_nombre = datos_actualizados.get('nombre', usuario_existente.nombre).upper()
            nuevo_apellido = datos_actualizados.get('apellido', usuario_existente.apellido).upper()
            nueva_edad = int(datos_actualizados.get('edad', usuario_existente.edad))
            nuevo_estado_civil = datos_actualizados.get('estado_civil', usuario_existente.estado_civil).lower()

            # Crea la nueva lista de fila
            filas[i] = [id_usuario, nuevo_nombre, nuevo_apellido, nueva_edad, nuevo_estado_civil]
            break

    if not encontrado:
        print(f"\n⚠️ Usuario con ID {id_usuario} no encontrado para actualizar.")
        return

    escribir_todas_las_filas(nombre_archivo, filas)
    print(f"\n✏️ Usuario con ID {id_usuario} actualizado con éxito.")