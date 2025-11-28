# # Ejercicios Listas y Tuplas

# # Ejercicios con Listas
# # 1. Rotación de Playlist Musical
# #Tienes una lista con el orden de canciones de una playlist
# Escribe un programa que pida al usuario un número n y rote la lista de canciones n posiciones a la derecha.
# # Ejemplo
# playlist = ["Canción A", "Canción B", "Canción C", "Canción D"]
# # Sin = 2 - ["Canción C", "Canción D", "Canción A", "Canción B"]

play_list = [f'\n1. Para que no me olvides\nJuan Fernando Velasco\n',
             f'\n2. Una flor\nAndrés Cepeda\n',
             f'\n3. Simples corazones\nFonseca\n',
             f'\n4. Un violinista en tu tejado\nMelendi\n',
             f'\n5. Sabrás\nHerencia de Timbiqui\n',
             f'\n6. Sin miedo a nada\nAlex Ubago\n']

# print(*play_list, sep= '\n')
def rotar_canciones():
    numero_para_rotar = int(input(f"ingresa un numero para rotar la lista: \n"))

    largo_de_playlist = len(play_list)

    n_rotar_play_list = numero_para_rotar % largo_de_playlist

    rotar_play_list = play_list[-n_rotar_play_list:] + play_list[:-n_rotar_play_list]

    print(f"\n-----------NUEVA PLAY LIST-----------------\n")
    print(*rotar_play_list, sep='\n')

# rotar_canciones()

# 2. Filtrar Ingredientes Prohibidos
# Un chef tiene una lista de ingredientes para una receta.
# Escribe un programa que pida al usuario los ingredientes que no quiere (pueden ser varios, separados
# por coma) y genere una nueva lista eliminando los ingredientes prohibidos.
# python
# CopiarEditar
# # Ejemplo

ingredientes = ["harina", "huevo", "leche", "azúcar", "chocolate","gelatina","huevo"]
# Prohibidos: huevo, leche -+ ["harina", "azúcar", "chocolate"]
# lo primero que debo hacer es revisar si el ingrediente_prohibido se en encuentra en ingredientes

def agregar_o_eliminar():

    def agregar():
        agregar_ingrediente = input(f"\ningrese un producto a adicionar a los ingredientes: \n").lower()
        ingredientes.append(agregar_ingrediente)
        print(f"\n{agregar_ingrediente} ha sido agregado")
    
    def eliminar ():
        ingrediente_prohibido = input(f"\nelimine un ingrediente de la lista ").lower()
        
        if ingrediente_prohibido in ingredientes:
            ingredientes.remove(ingrediente_prohibido)
            print(f"\n{ingrediente_prohibido} ha sido eliminado con exito")
        else:
            print(f"\nERROR,{ingrediente_prohibido}  no se encontro en ingredientes")
    while True:
        opcion = input(f"\ndeseas eliminar un ingrediente, selecciona con la letra 'E' o agregar un ingrediente selecciona con la letra 'A' o para salir de este menu 'S'\n").upper()
        
        if opcion == 'A':
            agregar()
        elif opcion == 'E':
            eliminar()
        elif opcion == 'S':
            break
        else:
            print("\nOpción no reconocida. Por favor, use 'A' , 'E' o 'S'.")
    
    print("\n--- INGREDIENTES FINALES ---")
    print(*ingredientes)
    print("------------------------------")
# agregar_o_eliminar()


# 3. Codificador por Saltos
# Crea un programa que reciba una lista de letras y un número salto,
# Debe generar una nueva lista con las letras saltando de acuerdo al valor dado.
# Ejemplo
#letras = ["a", "b", "c", "d", "e", "", "g"]
#salto = 2 -+ ["a", "c", "e", "g"]

letras_largas = [
    "A", "B", "C", "D", "E", 
    "F", "G", "H", "I", "J", 
    "K", "L", "M", "N", "O", 
    "P", "Q", "R", "S", "T", 
    "U", "V", "W", "X", "Y"
]
def codificador_por_saltos(letras, salto):
    return letras [::salto]

salto = input(f"\ningresa el numero de salto para codificar las letras: \n")
nueva_lista = codificador_por_saltos (letras_largas, int(salto))
print(f"\nla lista original de letras es: {letras_largas}")
print(f"\nla nueva lista codificada es: \n{nueva_lista}")

# 4. Eliminar Duplicados y Ordenar al Revés
# Dada una lista con números repetidos, crea un programa que elimine los duplicados y ordene los valores
# de mayor a menor.
# # Ejemplo
# numeros = [4, 2, 8, 4, 1, 8, 3] -+ [8, 4, 3, 2, 1]

numeros_repetidos = [
    5, 12, 8, 5, 20, 
    1, 12, 10, 8, 3, 
    5, 15, 20, 10, 8, 
    2, 12, 5, 1, 15, 
    7, 10, 3, 20, 12,
    5, 8, 15, 1, 20
]
def eliminar_duplicados_y_ordenar(numeros):
    numeros_repetidos = list(set(numeros))
    ordenar_numeros = sorted(numeros,reverse=True)
eliminar_duplicados_y_ordenar(numeros_repetidos)
# 5. Combinar Nombres y Apellidos
# Tienes dos listas: una de nombres y otra de apellidos.
# Escribe un programa que genere una nueva lista con el nombre completo de cada persona combinando
# ambas listas posición por posición.
# # Ejemplo
# nombres = ["Ana", "Luis", "Carla"]
# apellidos = ["Pérez", "Ramirez", "López"]
# # Resultado: ["Ana Pérez", "Luis Ramirez", "Carla López']
# Intercambio de Variables sin Variables Temporales
# Usando tuplas, intercambia los valores de dos variables sin usar una variable auxiliar.
# python
# CopiarEditar
# a, b = 5, 10
# # Resultado esperado: a = 10, b = 5
# Lista de Coordenadas y Distancia Máxima
# Dada una tupla de coordenadas (x, y) para varios puntos, encuentra los dos puntos más lejanos entre sí
# usando la fórmula de distancia euclidiana.
# python
# CopiarEditar
# puntos = ((0, 0), (2, 3), (5, 4), (7, 1))
# # Calcular la mayor distancia entre dos puntos
