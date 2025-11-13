# Ejercicios Listas y Tuplas
# Ejercicios con Listas
# 1. Lista de compras básica
#    o Crea una lista con 5 productos de supermercado y muéstrala en pantalla.

# productos = ["CHOCOLATE","CAFE","AZUCAR","LECHE","PAN"]
# print(productos)
# print (type(productos))

# # 2. Modificar tu pedido
# #   o Tienes una lista con 4 comidas favoritas, cambia la segunda por un nuevo platillo.

# comidas_favoritas = ["arroz chino","ramen","sushi","lechona"]
# print(comidas_favoritas)
# comidas_favoritas[1]="sopa"
# print(comidas_favoritas)

# # 3. Agregar y quitar invitados
# #   o Crea una lista con 3 invitados a una fiesta, agrega dos más, y luego elimina uno.

# invitados = ["paula","juliana","carolina"]
# print(invitados)
# invitados.extend(["felipe","luis"]) 
# print(invitados)
# invitados.remove("paula")

# # 4. Lista inversa
# #   o Crea una lista con 5 colores y muestra la lista en orden inverso usando reverse() o [::-1].

# colores = ["amarillo","rojo","azul","blanco","purpura"]
# print(f"\nlista original: {colores}")
# colores.reverse()
# print(f"\nprimer inverso: {colores}")
# colores_inverso = colores[::-1]
# print(f"\nlista original al reversar con la función ::-1 {colores_inverso}")

# # 5. Contando animales
# #   o Crea una lista con animales y usa len() para mostrar cuántos hay.

# animales = ["leon","tigre","vaca","oveja","abeja","elefante"]
# print(f"\nlistado de aminales es: {animales}")
# contar_animales =len(animales)
# print(f"\nla cantidad de animales en la lista es {contar_animales}")

# # 6. Duplicados fuera
# #   o Crea una lista con elementos repetidos y usa set() para mostrar la lista sin duplicados.

# lista_combinada = [1,54,True,False,"andres","eduardo","ANDRES","rojas",1,54,True]
# print(f"\n{lista_combinada}")
# lista_limpia = set(lista_combinada)
# print(f"\nla lista sin datos repetido es esta {lista_limpia}")

# # 7. Números al cuadrado
# #   o Crea una lista de números y genera una nueva lista con el cuadrado de cada número usando un bucle o comprensión de listas.

# lista = [1,2,3,4,5,6,7,8,9,10,11]
# nueva_lista = [numero ** 2 for numero in lista ]
# print(f"\nla lista original es igual a {lista}"
#       f"\nla nueva lista con los datos duplicados es igual: {nueva_lista}")

# # 8. Lista combinada
# #    o Une dos listas (por ejemplo, frutas y verduras) en una sola y muéstrala.

# Frutas = ['Manzana', 'Naranja', 'Plátano', 'Pera', 'Uva', 'Fresa', 'Limón', 'Pomelo', 'Mango', 'Piña', 'Aguacate', 'Cereza', 'Arándano']
# Verduras = ['Lechuga', 'Espinaca', 'Zanahoria', 'Papa', 'Brócoli', 'Coliflor', 'Tomate', 'Pepino', 'Pimiento', 'Cebolla', 'Ajo', 'Calabacín', 'Rábano']

# fruver =Frutas + Verduras

# print (fruver)

# # 9. Eliminar por condición
# #   o De una lista de números, elimina todos los que sean menores a 5.

# numeros_originales = [1, 10, 3, 7, 2, 9, 4, 12, 5, 0]
# lista_filtrada = [numero for numero in numeros_originales if numero >= 5]
# print("Lista original:", numeros_originales)
# print("Lista filtrada:", lista_filtrada)

# 10. Simulación de inventario
#   o Crea una lista que represente el inventario de una tienda. Permite que el usuario agregue y quite productos mediante input().

inventario = ["papel","lapiz","borrador","esfero","cuaderno","libro","grapas"]

def agregar_o_eliminar():

    def agregar():
        producto_a_añadir = input(f"\ningrese un producto adicional al inventario: \n").lower()
        inventario.append(producto_a_añadir)
        print(f"\n{producto_a_añadir} ha sido agregado")
    
    def eliminar ():
        producto_a_eliminar = input(f"\nelimine un producto de la lista ").lower()
        if producto_a_eliminar in inventario:
            inventario.remove(producto_a_eliminar)
            print(f"\n{producto_a_eliminar} ha sido eliminado con exito")
        else:
            print(f"\nERROR,{producto_a_eliminar}  no se encontro en el inventario")

    
    opcion = input(f"\ndeseas eliminar selecciona con la letra 'E' o agregar un producto selecciona con la letra 'A' ").upper()
    
    if opcion == 'A':
        agregar()
    elif opcion == 'E':
        eliminar()
    else:
        print("\nOpción no reconocida. Por favor, use 'A' o 'E'.")
    
    print("\n--- INVENTARIO ACTUALIZADO ---")
    print(inventario)
    print("------------------------------")

#agregar_o_eliminar()

#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# Ejercicios creativos con tuplas
# 1. Tupla de coordenadas
#   o Crea una tupla que represente la ubicación (x, y) de un punto y muéstrala.
coordenada_x_y = (3,7)
print(f"\n{coordenada_x_y}")
print(type(coordenada_x_y))

# 2. Datos de una persona
#   o Crea una tupla con nombre, edad y ciudad, y muestra cada elemento con su etiqueta.
Datos_personales =("ANDRES",15,"BOGOTÁ")
NOMBRE, EDAD , CIUDAD = Datos_personales
print(F"\n----INFORMACIÓN PERSONAL----"
F"\n NOMBRE: {NOMBRE}"
F"\n EDAD: {EDAD}"
F"\n CIUDAD: {CIUDAD}"
"\n-------------------------")

# 3. Desempaquetando frutas
#   o Crea una tupla con 3 frutas y asígnalas a tres variables diferentes.

frutas = ("Manzana", "Naranja", "Plátano", "Fresa", "Mango", "Uva", "Kiwi")
rojo1 , naranja , amarillo1 , rojo2 , amarillo2 , morado , verde = frutas
print(f"\n{frutas}")
print(f"\nla fruta {rojo1} es de color rojo"
      f"\nla fruta {naranja} es de color naranja"
      f"\nla fruta {morado} es de color morado")

# 4. No se puede cambiar
#   o Intenta modificar una tupla y explica por qué da error.

# añadir_fruta = input(f"\ningrese una fruta adicional al inventario: \n").lower()
# frutas.append(añadir_fruta)       #las tuplas tienen como caracteristica que no son mutables, por 
# print(f"\n{frutas} ha sido agregado")  # lo que no deja modificar su informcación de ninguna manera

# 5. Concatenar tuplas
#   o Crea dos tuplas y únelas en una sola.
fibonacci = (1, 1, 2, 3, 5, 8, 13)
colores_primarios = ("Rojo", "Azul", "Amarillo")
concatenar =fibonacci + colores_primarios
print(f"\nel resultado de concatenar dos tuplas es {concatenar}")

# 6. Tupla repetida
#   o Crea una tupla pequeña y repítela 3 veces usando el operador *.

tupla_pequeña = (3,5,2,56)
repetir_tupla = tupla_pequeña * 3 
print(f"\nel resultado de repetir una tupla pequeña es :{repetir_tupla}")

# 7. Máximo y mínimo
#   o Crea una tupla de números y encuentra el valor mayor y menor usando max() y min().
tupla_numero = (1,2,3,4,5,5,6,7,8,9,10,11,12,13,14,15,16,17,18)
mayor = max(tupla_numero)
menor = min(tupla_numero)
print(f"\nEl numero de mayor tamaño en la tupla= {tupla_numero}"
      f"\nes: {mayor}"
      f"\ny el numero de menor tamaño es: {menor}")

# 8. Convertir lista a tupla
#   o Crea una lista y conviértela a tupla con tuple().
lista_a_tupla = [1,432,5432,"datos","ramdom", True,False]
tupla_nueva =tuple(lista_a_tupla)
print((f"la clase de la lista modifica con tuple es {type(tupla_nueva)}"))

# 9. Buscar elemento
#   o Crea una tupla y verifica si un elemento está en ella usando in.
# Definición de la tupla de productos
b_tupla = ("arroz", "cafe", "leche", "banano", "aguacate", "azucar")

def manejar_busquedas(lista_productos):
    
    #Permite al usuario realizar múltiples búsquedas hasta que decida salir.
    
    print("\n--- Iniciando el buscador de productos ---")
    
    while True:
        producto_a_buscar = input(
            "\nIngresa el producto que deseas buscar (o 'salir' para terminar): ").lower().strip()
        
        # 1. Manejar la entrada vacía
        if not producto_a_buscar:
            print("Error: No has ingresado ningún dato.")
            continue # Vuelve al inicio del bucle
        
        # 2. Manejar la salida
        if producto_a_buscar == "salir":
            print("¡Hasta luego! Terminando el programa.")
            break # Sale del bucle principal
        
        # 3. Realizar la búsqueda
        if producto_a_buscar in lista_productos:
            print(f"¡El producto **{producto_a_buscar.capitalize()}** se encuentra en la lista!")
        else:
            print(f"Lo sentimos, no encontramos el producto **{producto_a_buscar.capitalize()}** que estás buscando.")


# 10. Índice de un elemento
#   o Crea una tupla y encuentra la posición de un elemento con .index().   
