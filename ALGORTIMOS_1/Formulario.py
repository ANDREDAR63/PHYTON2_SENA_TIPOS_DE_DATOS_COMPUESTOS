#edad = int(input("ingrese su edad:"))
#print ("tu edad es:",edad)
#==============FORMULARIO========

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
    print(f"Hola, "+nombre_completo.lower()+". Tu correo corporativo sugerido es: "+correo_corporativo)
    return nombre_completo 
nombre_del_usuario = solicitar_nombre()

"""
#===============DATOS NUMERICOS=========
edad =int(input("ingrese su edad"))
peso =float(input("Ingresa su peso"))
telefono =int(input("ingrese su telefono"))
altura =float(input ("ingrese su altura"))
hijos =int(input("ingrese el numero de hijos"))
año_nacimiento=int(input("ingrese su año de nacimiento"))
mes_nacimiento=int(input("ingrese su mes de nacimiento"))
dia_nacimiento=int(input("ingrese su dia de nacimiento"))
cedula=int(input("ingrese su numero de cedula"))
#==============DATOS TEXTO O STRING=============
correo = input("ingrese su correo")
tipo_sangre=input("ingrese su tipo de sangre")
genero = input("ingrese su genero")
estado = input("ingrese si es casada o soltera")
eps=input("ingrese su eps")
universidad = input("ingrese su universidad")
carrera = input("ingrese su carrera")
"""