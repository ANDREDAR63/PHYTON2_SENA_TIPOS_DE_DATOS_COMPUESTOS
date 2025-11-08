#1. Declaración simple: Crea tres variables (nombre, edad, altura) y asígnales valores adecuados. Imprime sus valores.
nombre = "ANDRES EDUARDO"
edad = 24
altura = 1.69
print ("mi nombre es ",nombre.lower(), "tengo ",edad,"años y mido",altura,"metros")
#2. Identificar tipo: Declara variables de tipo entero, flotante, cadena y booleano. Usa type() para mostrar su tipo.
entero = 12
flotante = 3.14159
cadena = "cadena de texto"
booleano = True
print("el tipo de dato de los enteros es :",type(entero))
print("el tipo de dato de los flotantes es :",type(flotante))
print("el tipo de dato de cadena es :",type(cadena))
print("el tipo de dato de los booleanos es :",type(booleano))
#3. Concatenación: Declara dos variables de texto con tu nombre y apellido. Combínalas en una sola variable e imprímela.
nombre = "ANDRES EDUARDO"
apellido = "ROJAS GONZALEZ"
nombre_completo = nombre + " " + apellido
print(nombre_completo)
#4. Operaciones numéricas: Declara dos variables numéricas y muestra la suma, resta, multiplicación y división.
a = 12
b = 32
c = a + b
print ("la suma de a y b es igual a :", c)
r = a - b
print (f"la resta de a y b es igual a :", r)
m = a * b 
print ("la multiplicacion de a y b es igual a :", m)
d = a / b
print ("la division de a y b es igual a :", d)
# 5. Booleanos: Crea dos variables booleanas y usa operadores
x = True
y = False

resultado_and_1 = x and x # 1. x and x: True y True -> True (Ambos son True)
print(f"En and True and True = {resultado_and_1}")
resultado_and_2 = x and y # 2. x and y: True y False -> False (Uno es False)
print(f"En and True and False = {resultado_and_2}")
resultado_and_3 = y and x # 3. y and x: False y True -> False (Uno es False)
print(f"En and False and True = {resultado_and_3}")
resultado_4 = y and y # 4. y and y: False y False -> False (Ambos son False)
print(f"En and False and False = {resultado_4}")

val1 = 14
val2 = 13
bool1 = val1 == val2
bool2 = val1 != val2

if bool1 and bool2:
    print("es verdadero")
else:
    print("es falso")