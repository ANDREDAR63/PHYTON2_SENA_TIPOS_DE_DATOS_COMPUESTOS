#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#OPERADORES EN PYTHON
# OPERADORES ARITMETICOS
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
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# OPERADORES RELACIONALES
igualdad = a == b
Desigualdad = a != b
Mayor_a_la_derecha = a > b
Menor_a_la_derecha = a < b
Mayor_o_igual = a >= b
Menor_o_igual = a <= b
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# OPERADORES LOGICOS

x = True
y = False
# COMPARADOR AND
resultado_and_1 = x and x # 1. x and x: True y True -> True (Ambos son True)
print(f"En and True and True = {resultado_and_1}")
resultado_and_2 = x and y # 2. x and y: True y False -> False (Uno es False)
print(f"En and True and False = {resultado_and_2}")
resultado_and_3 = y and x # 3. y and x: False y True -> False (Uno es False)
print(f"En and False and True = {resultado_and_3}")
resultado_4 = y and y # 4. y and y: False y False -> False (Ambos son False)
print(f"En and False and False = {resultado_4}")
# COMPARADOR OR
resultado_or_1 = x or x # 1. x or x: True o True -> True (Ambos son True)
print(f"En or True or True = {resultado_or_1}")
resultado_or_2 = x or y # 2. x or y: True o False -> True (Al menos uno es True)
print(f"En or True or False = {resultado_or_2}")
resultado_3 = y or x # 3. y or x: False o True -> True (Al menos uno es True)
print(f"En or False or True = {resultado_3}")
resultado_4 = y or y # 4. y or y: False o False -> False (Ambos son False)
print(f"En or False or False = {resultado_4}")
# COMPARADOR NOT
resultado_not_1 = not x # 1. not x: no True -> False (Invierte el valor de x)
print(f"not True = {resultado_not_1}")
resultado_not_2 = not y # 2. not y: no False -> True (Invierte el valor de y)
print(f"not False = {resultado_not_2}")

#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# OPERADORES UNARIOS
z = 7
print("z es positivo",{+z})
print("z es negativo",{-z})
print("not z > 0",{not(z)})

