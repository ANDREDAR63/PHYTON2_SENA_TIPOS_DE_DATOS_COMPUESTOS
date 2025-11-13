#1. Suma de dos números: Pide dos números y muestra su suma.

def suma():
    print("\n--- SUMA DE DOS NUMEROS---\n\n") 
    Nmro_1 = input("Ingresa un numero para sumar: ")
    while not Nmro_1:
        Nmro_1 = input("\nPor favor ingresa un numero para sumar: ")

    Nmro_2 = input("\nIngrese el segundo numero para sumar: ")
    while not Nmro_2:
        Nmro_2= input("\nPor favor ingresa el segundo numero para sumar: ")

    NUMERO_1=float(Nmro_1)
    NUMERO_2= float(Nmro_2)
    SUMAR = float(NUMERO_1 + NUMERO_2) 
    numero_redondeado = round(SUMAR,3)
    print("\n--- RESULTADO ---")
    print(f"\n{numero_redondeado}\n\n\n")
    return numero_redondeado 

# resultado_suma = suma()

#3. Área del triángulo: Calcula el área de un triángulo con base y altura ingresadas por el usuario.

def area_de_un_triangulo():
    print("\n--- CALCULA EL ÁREA DE UN TRIANGULO ---\n\n") 

    IN_Base = input("Ingresa la medida de la base de tu triangulo: ")
    while not IN_Base:
        IN_Base = input("\nPor favor ingresa la medida de la base de tu triangulo: ")
    
    IN_altura = input("\nIngrese la medida de la altura de tu triangulo: ")
    while not IN_altura:
        IN_altura= input("\nPor favor in    gresa la medida de la altura de tu triangulo: ")
    
    altura=float(IN_altura)
    Base= float(IN_Base)

    area = (Base
         * altura) / 2

    area_redondeada = round(area,3)
    print("\n--- RESULTADO ---")
    print(f"\nEl área de tu triángulo es: base = {Base} x altura = {altura} ÷ 2 = {area_redondeada}")
    return area_redondeada
# B_x_A_d_2 = area_de_un_triangulo()


#5. Potencia: Calcula xyx^yxy usando el operador **

def Potenciacion():
    print("\n--- POTENCIACION DE DOS NUMEROS---\n\n") 
    Nmro_1 = input("Ingresa un numero para potenciar: \n")
    while not Nmro_1:
        Nmro_1 = input("\nPor favor ingresa un numero para potenciar: ")
    Nmro_2 = input("\nIngrese el segundo numero para potenciar: ")
    while not Nmro_2:
        Nmro_2= input("\nPor favor ingresa el segundo numero para potenciar: ")
    NUMERO_1=float(Nmro_1)
    NUMERO_2= float(Nmro_2)
    POTENCIAR = float(NUMERO_1 ** NUMERO_2)
    numero_redondeado = round(POTENCIAR,3)
    print("\n--- RESULTADO ---")
    print(f"\n{numero_redondeado}\n\n\n")
    return numero_redondeado 
# resultado_potencia = Potenciacion()

#7. Verificar edad: Pide la edad y muestra si la persona es mayor de edad (≥18).

def Mayor_de_edad() :
    while True:
        edad_str = input ("\nPor favor ingresa tu edad: ")
        if not edad_str:
            print ("\nNo has ingresado ningún dato")
            continue
        try:
            edad_num = int(edad_str)
            break
        except ValueError:
            print("\n!ERROR¡, ingresa un número valido")
    print(f"\nTu edad es {edad_num}\n")

    if edad_num >= 18 :
        print("\nEres mayor de edad")
    else: print("\nEres menor de edad")

    if edad_num >= 18 :
        mayor_de_edad = True
    else: mayor_de_edad = False

    return mayor_de_edad
# resultado_edad = Mayor_de_edad ()

#9. Comparar cadenas: Pide dos cadenas y verifica si son iguales.

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

            if not revisar_mayusculas(nueva_contraseña) :
                print("\ntu contraseña requiere al menos una letra mayuscula")
                contraseña_valida=False

            if not revisar_minusculas(nueva_contraseña) :
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

#11. Acceso de usuario: Pide un nombre de usuario y contraseña, y verifica si coinciden con valores predefinidos.

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

#13. Verificación múltiple: Pide tres valores booleanos e imprime si al menos uno es True (usa or).

# val_1 = Mayor_de_edad()
# val_2 = input("\n¿tiene nacionalidad colombiana? (si/no): ").strip().lower()
# val_3 = input("\n¿pertenece a algun grupo poblacional específico (indígena, pelenquero, desplazado, etc.)? (si/no): ").strip().lower()

# if val_2 == "si":
#     val_2 = True
# else:
#     val_2 = False

# if val_3 == "si":
#     val_3 = True
# else:
#     val_3 = False



#15. Combinación: Determina si un número está entre 10 y 50 y es par al mismo tiempo.

# print("\n--- VERIFICAR SI UN NUMERO ESTA ENTRE 10 Y 50 Y ES PAR ---\n\n")
# numero = int(input("\nIngresa un numero entero: "))
# cumple_la_condicion = (10 <= numero <=50) and (numero % 2 ==0)

# if cumple_la_condicion:
#     print("este numero no cumple la condicion")
# else:
#     print("este numero no cumple la condicion")

#17. Descuento: Crea una variable precio, aplica un 20% de descuento usando *= y muestra el nuevo valor.
precio = float(input("\nIngrese el precio del producto: "))
descuento = 0.20        
precio *= (1 - descuento)  
precio_redondeado = round(precio, 2)
print(f"\nEl precio con el descuento aplicado es: {precio_redondeado}\n")

#19. AND bit a bit: Pide dos números enteros y muestra el resultado de &amp;. 
num1 = int(input("\nIngrese el primer número entero: "))
num2 = int(input("\nIngrese el segundo número entero: "))

resultado = num1 & num2

print(f"\nEl resultado de {num1} & {num2} es: {resultado}\n")
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::