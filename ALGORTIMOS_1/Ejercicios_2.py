#======================================
# 1. Contar cuántos caracteres tiene la frase (incluyendo espacios)
frase = "Hola mundo"
print(len(frase))
# 2. Convertir el nombre a mayúsculas
nombre = "juan perez"
print((nombre).upper())

# 3. Contar cuántas veces aparece la letra "a" en el texto
texto = "La casa está vacía"
print(texto.count("a"))
# 4. Mostrar la palabra repetida 5 veces, separada por espacios
palabra = "Python "
veces = 5
resultado1 = palabra * veces
print(resultado1)

# 5. Mostrar la última letra de la cadena
mensaje = "Programación"
print(mensaje[-1])
# 6. Mostrar la cadena al revés
cadena = "Hola Mundo"
print(cadena[::-1])
# 7. Reemplazar "Java" por "Python" en la frase
frase = "Me gusta Java"
print(frase.replace("Python","Java"))
# 8. Mostrar solo los primeros 4 caracteres del título
titulo = "Introducción"
print(titulo[0:4])
# 9. Contar cuántas palabras tiene la oración (separadas por espacios)
oracion = "Python es divertido"
lista_de_plabras= oracion.split()
print(lista_de_plabras)
contar_palabras= len(lista_de_plabras)
print(contar_palabras)
# 10. Convertir la cadena a formato título → "El Señor De Los Anillos"
libro = "el señor de los anillos"
print(libro.title())
# 11. Quitar los espacios en blanco al inicio y al final del saludo
saludo = "   Hola mundo   "
contar_plabras_2 = saludo.strip()
print(contar_plabras_2)

# 12. Verificar si la cadena contiene solo letras (sin números ni símbolos)
codigo = "Python3"
verificar = codigo.isalpha()
print(verificar)

# 13. Mostrar las iniciales del nombre completo → "C.A.G."
nombre_completo = "Carlos Alberto García"

# 14. Reemplazar las vocales con "_" (guion bajo)
frase = "Estoy aprendiendo Python"
vocales = "AEIOUaeiouYy"
resultado = ""
for letra in frase:
    if letra in vocales:
        resultado += "_"
    else:
        resultado += letra

print(resultado) 

# 15. Crear un nombre de usuario con las 2 primeras letras del nombre + 3 últimas del apellido, en minúsculas
nombre = "Luis"
apellido = "Martínez"
