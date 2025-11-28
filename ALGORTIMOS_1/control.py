#--------------------------CONTROL----------------------------
#---------------CICLO O BUCLE FOR-----------------------------
for i in range (1,6):
    print(f"El valor de i es: {i}")
#------------------(EJEMPLOS)-----------------------------------

LISTA = ["MELON", "MANZANA", "PERA", "BANANO", "FRESA"]
for FRUTAS in LISTA:
    print(f"LA FRUTA ES: {FRUTAS}")

#------------------(WHILE)---------------------------------
contador = 1
while contador <= 10:

    print(f"El valor del contador es: {contador}")
    contador += 1

#------------------(IF)----------------------------------
Edad = 18
if Edad >= 18:
    print("Eres mayor de edad")
#----------------(ELSE)--------------------------------
else:
    print("Eres menor de edad") 
#----------------(IF-ELSE)--------------------------------
numero = int(input("Ingresa un numero: \n"))
if numero % 2 == 0:
    print(f"El numero {numero} es par")
else:
    print(f"El numero {numero} es impar")


