#cadena de caracterres se refiere a una cadena de datos que ocupa un espacio de memoria
#carateres (a) (1) (datos) y si se unen forman cadenas de caracteres
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
print ("hola mundo")
print ("ANDRES ROJAS GONZALEZ")
curso = "programacion uno"
print ("su curso es:", curso)
institucion = "SENA" # variable tipo string
print ("su curso es :",curso,"su institución es:", institucion)
trimestre = 1 # variable tipo integreer
print ("su curso es :",curso,"su institución es:", institucion, "su trimestre es:",trimestre) # imprimir carias variables
print(len(institucion)) # el comando len es para contar los caracteres
print (len(curso))
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
print(curso.upper())# el comando .upper es para poner la cadena de texto en mayuscula
print(curso.lower())# el comando .lower es para poner la cadena de texto en minuscula
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
print(institucion[0])# loas corchetes sirven para traer la posicion de un caracter dentro de la cadena de texto
print(institucion[1])
print(institucion[2])
print(institucion[3])
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
print(institucion[0:3]) # los corhcetes mas : sirven para traer un ragno de la cadena de texto
# concatenar= unir dos cadenas de texto que estan separadas
print((institucion + ""+ curso).upper())
#comparar una cadena
print(curso == institucion)
print("Analisis y desarrollo de sistemas".replace("sistemas","software"))
# RETO: CREAR CORREO INSTITUCIONAL QUE INCIE CON LA PRIMER LETRA DEL NOMBRE LA PRIMERA DEL SEGUNDO NOMBRE Y EL PRIMER APELLIDO COMPLETO
primer_nombre_empleado = "ANDRES"
segundo_nombre_empleado = "FERNANDA"
primer_apellido_empleado = "CHAVARRO" 
segundo_apellido_empleado = "QUINTERO"
correo_corporativo = ("su correo corporativo es: "+(primer_nombre_empleado[0]+segundo_nombre_empleado[0]+primer_apellido_empleado+segundo_apellido_empleado[0]).lower()+"@sena.edu.co")
print(correo_corporativo)