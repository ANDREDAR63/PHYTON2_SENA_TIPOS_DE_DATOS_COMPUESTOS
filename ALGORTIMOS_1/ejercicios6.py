def cepillar_dientes():
    while True:
        primero = "ingresar al baño"
        segundo = "tomar el cepillo de dientes"
        tercero = "aplicar pasta dental"
        cuarto = "cepillar los dientes"
        quinto = "enjuagar la boca"    
        sexto = "salir del baño"
        cepillar_dientes_t = True
        if not  primero:
            print("Debes ingresar al baño primero.")
            cepillar_dientes_t == True
        if not segundo:
            print("Debes tomar el cepillo de dientes.")
            cepillar_dientes_t == True
        if not tercero:
            print("Debes aplicar pasta dental.")
            cepillar_dientes_t == True
        if not cuarto:
            print("Debes cepillar los dientes.")
            cepillar_dientes_t == True
        if not quinto:
            print("Debes enjuagar la boca.")
            cepillar_dientes_t == True
        if not sexto:
            print("Debes salir del baño.")
            cepillar_dientes_t == True

        if cepillar_dientes_t == True:
            print("Has cepillado tus dientes correctamente.")
            break
        else:
            print("Intenta cepillar tus dientes de nuevo.")
usuarios = []
def Agregar_usuarios():
    id_usuarios = int(input("Ingrese su id de usuario: \n"))
    nombre_usuarios = input("Ingrese su nombre de usuario: \n").upper()
    apellido_usuarios = input("Ingrese su apellido de usuario: \n").upper()
    edad_usuarios = int(input("Ingrese su edad: \n"))
    estado_civil = input("Ingrese su estado civil: \n").lower()
    usuario = {
        "id": id_usuarios,
        "nombre": nombre_usuarios,
        "apellido": apellido_usuarios,
        "edad": edad_usuarios,
        "estado_civil": estado_civil
    }
    usuarios.append(usuario)
    print("Usuario agregado con éxito.")
    return usuario
Agregar_usuarios()
print(*usuarios,sep="\n")