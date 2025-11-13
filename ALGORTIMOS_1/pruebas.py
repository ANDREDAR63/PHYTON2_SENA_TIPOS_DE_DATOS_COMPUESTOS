def solicitar_nombre():
    print("\n--- FORMULARIO DE USUARIOS ---\n\n") 
    nombre_1 = input("Ingrese su primer nombre: ")
    while not nombre_1:
        nombre_1 = input("\nPor favor ingresa tu nombre: ")
    nombre_2 = input("\nIngrese su segundo nombre: ")
    apellido_1 = input("\nIngrese su primer apellido: ")
    while not apellido_1:
        apellido_1 = input("\nPor favor ingresa tu primer apellido: ")
    apellido_2 = input("\nIngrese su segundo apellido: ")
    nombre_completo = f"{nombre_1} {nombre_2} {apellido_1} {apellido_2}"
    inicial_nombre_1 = nombre_1[0] if nombre_1 else '' 
    inicial_nombre_2 = nombre_2[0] if nombre_2 else nombre_1[1]
    inicial_apellido_2 = apellido_2[0] if apellido_2  else apellido_1[-1]
    correo_corporativo = (
        inicial_nombre_1 + 
        inicial_nombre_2 + 
        apellido_1 + 
        inicial_apellido_2).lower() + "@sena.edu.co"
    print("\n--- RESULTADO ---")
    print(f"\nNombre completo: {nombre_completo}")
    print(f"Hola, "+nombre_completo.lower()+". Tu correo corporativo es: "+correo_corporativo)
    return correo_corporativo 
# nombre_del_usuario = solicitar_nombre()
#esta funcion es para revisar si hay simbolos en una cadena de texto

def revisar_simbolos(cadena_de_simbolos):
    for caracter in cadena_de_simbolos:
        if caracter.isspace():
            continue 
        if not caracter.isalnum():
            return True
    return False


#esta funcion es para revisar si hay numeros en una cadena de texto

def revisar_numeros(cadena_de_texto):
    for caracter in cadena_de_texto:
        if  caracter.isdigit():
            return True 
    return False

#esta funcion es para revisar si hay letras en una cadena de texto

def revisar_letras(cadena_de_texto):
    for caracter in cadena_de_texto:
        if  caracter.isalpha():
            return True 
    return False

#esta funcion es para revisar si hay mayusculas en una cadena de texto

def revisar_mayusculas(cadena_de_texto):
    for caracter in cadena_de_texto:
        if  caracter.isupper():
            return True 
    return False

#esta funcion es para revisar si hay minusculas en una cadena de texto

def revisar_minusculas(cadena_de_texto):
    for caracter in cadena_de_texto:
        if  caracter.islower():
            return True 
    return False

def creacion_de_contraseñas ():# SE USARA COMO EJEMPLO EL USO DE CONTRASEÑAS
    while True:    
        while True:
            print("\nCrea tu nueva contraseña, por razones de seguridad tu contraseña tiene que tener las siguientes caracteristicas:\n" \
            "* minimo 8 caracteres\n" \
            "* minimo una mayuscula\n" \
            "* minimo un simbolo\n" \
            "* minimo un número\n")
            nueva_contraseña =input("\ningresa una nueva contraseña: \n")

            if not nueva_contraseña: 
                print("\nno has ingresado ningun dato\n")
                continue
            
            contraseña_valida = True

            if not revisar_simbolos(nueva_contraseña):
                print("\nnecesitas al menos un simbolo en tu contraseña")
                contraseña_valida=False

            if not revisar_numeros(nueva_contraseña):
                print("\ntu contraseña requiere al menros un numero")
                contraseña_valida=False

            if not revisar_mayusculas(nueva_contraseña) == True:
                print("\ntu contraseña requiere al menos una letra mayuscula")
                contraseña_valida=False

            if not revisar_minusculas(nueva_contraseña) == True:
                print("\ntu contraseña requiere al menos una letra minuscula")
                contraseña_valida=False
            
            if len(nueva_contraseña) < 8:
                print("\nContraseña válida.")
                contraseña_valida=False
            
            if contraseña_valida:
                print("\ntu contraseña es valida\n")
            else: print("\nrevisa tu contraseña e intenta nuevamente")
            break

        while True:   
            validacion_nueva_contraseña =input("\npor favor confirma tu nueva contraseña: \n")
            if validacion_nueva_contraseña:
                break
            print("\nno has ingresado ningun dato\n")
            

        if nueva_contraseña == validacion_nueva_contraseña:
                print("\nnueva contraseña asignada con exito\n")
                break
        else:print("\ntus contraseñas no son iguales, por favor verifica los datos e intenta nuevamente\n")
    return nueva_contraseña 
# resultado_comparar_str = creacion_de_contraseñas()

# USUARIO = solicitar_nombre()
# CONTRASEÑA = creacion_de_contraseñas()

def ingreso_de_sesion(U, C):
    print("\n::::::::::::::::::::: BIENVENIDO, POR FAVOR INGRESA TUS DATOS DE ACCESO :::::::::::::::::::::::::\n")

    while True:
        VAL_USUARIO = input("\nUSUARIO = ")
        VAL_CONTRASEÑA = input("\nCONTRASEÑA = ")
        
        if VAL_USUARIO == U and VAL_CONTRASEÑA == C:
            print(f"\nBienvenido {U}\n")
            break
        elif VAL_USUARIO != U:
            print("USUARIO INCORRECTO. INTÉNTELO DE NUEVO.\n")
        else:
            print("CONTRASEÑA INCORRECTA. INTÉNTELO DE NUEVO.\n")

# ingreso_de_sesion(USUARIO,CONTRASEÑA)
