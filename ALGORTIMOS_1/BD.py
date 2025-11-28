import csv # importar la librería csv para manejar archivos CSV 
with open('usuarios.csv',"w",newline="") as archivo_crear un objeto escritor CSV
    escritor_csvsv: # abrir el archivo en modo de agregar
    escritor_csv = csv.writer(archivo_csv) # c.writerow(['id','nombre','apellido','edad','estado_civil']) # escribir la fila de encabezado
    def Agregar_usuarios(): # definir la función para agregar usuarios
        id_usuarios = int(input("Ingrese su id de usuario: \n")) # solicitar el id del usuario
        nombre_usuarios = input("Ingrese su nombre de usuario: \n").upper() # solicitar el nombre del usuario y convertirlo a mayúsculas
        apellido_usuarios = input("Ingrese su apellido de usuario: \n").upper() # solicitar el apellido del usuario y convertirlo a mayúsculas
        edad_usuarios = int(input("Ingrese su edad: \n")) # solicitar la edad del usuario
        estado_civil = input("Ingrese su estado civil: \n").lower() # solicitar el estado civil del usuario y convertirlo a minúsculas
        usuario = { # crear un diccionario con los datos del usuario
            "id": id_usuarios,
            "nombre": nombre_usuarios,
            "apellido": apellido_usuarios,
            "edad": edad_usuarios,
            "estado_civil": estado_civil
        }
        escritor_csv.writerow([id_usuarios, nombre_usuarios, apellido_usuarios, edad_usuarios, estado_civil]) # escribir los datos del usuario en el archivo CSV
        print("Usuario agregado con éxito.") # imprimir mensaje de éxito
        return usuario # retornar el diccionario del usuario
    Agregar_usuarios() # llamar a la función para agregar un usuario

    def eliminar_usuarios(id_usuario): # definir la función para eliminar usuarios
        archivo_csv.seek(0) # mover el cursor al inicio del archivo
        filas = list(csv.reader(archivo_csv)) # leer todas las filas del archivo CSV
        filas_actualizadas = [fila for fila in filas if fila[0] != str(id_usuario)] # filtrar las filas para eliminar el usuario con el id especificado
        archivo_csv.truncate(0) # vaciar el archivo
        escritor_csv.writerows(filas_actualizadas) # escribir las filas actualizadas en el archivo CSV
        print(f"Usuario con id {id_usuario} eliminado con éxito.") # imprimir mensaje de éxito
    
    def actualizar_usuarios(id_usuario): # definir la función para actualizar usuarios
        archivo_csv.seek(0) # mover el cursor al inicio del archivo
        filas = list(csv.reader(archivo_csv)) # leer todas las filas del archivo CSV
        for i, fila in enumerate(filas): # iterar sobre las filas con su índice
            if fila[0] == str(id_usuario): # si el id de la fila coincide con el id especificado
                nombre_usuarios = input("Ingrese su nuevo nombre de usuario: \n").upper() # solicitar el nuevo nombre del usuario
                apellido_usuarios = input("Ingrese su nuevo apellido de usuario: \n").upper() # solicitar el nuevo apellido del usuario
                edad_usuarios = int(input("Ingrese su nueva edad: \n")) # solicitar la nueva edad del usuario
                estado_civil = input("Ingrese su nuevo estado civil: \n").lower() # solicitar el nuevo estado civil del usuario
                filas[i] = [id_usuario, nombre_usuarios, apellido_usuarios, edad_usuarios, estado_civil] # actualizar la fila con los nuevos datos
                break
        archivo_csv.truncate(0) # vaciar el archivo
        escritor_csv.writerows(filas) # escribir las filas actualizadas en el archivo CSV
        print(f"Usuario con id {id_usuario} actualizado con éxito.") # imprimir mensaje de éxito
    
    def ver_usuarios(): # definir la función para ver usuarios
        archivo_csv.seek(0) # mover el cursor al inicio del archivo
        lector_csv = csv.reader(archivo_csv) # crear un objeto lector CSV
        for fila in lector_csv: # iterar sobre las filas del archivo CSV
            print(fila) # imprimir cada fila
    
    