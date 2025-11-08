#TIPOS DE DATOS SIMPLES
string = f"son los datos que corresponden a cadenas de texto" #se usa "" o '' para decirle al sistema que se trata de un dato tipo texto en una sola linea, 
#cuado quieres escribir cadenas de texto en mas de una linea se usa """ """ o ¨¨
integrer = -3,-2,-1,0,1,2,3,4,5,16,2654,7536, #los integrer son datos que pertenecen al grupo de los numeros enteros
los_float = 3.14154245 , 10,54325 , 432.43143214  #los float son un tipo de dato que correponde a numeros decimales los cuales se deben escribir con punto no con coma 
#la coma es para separar datos
booleam = True , False # los datos booleanos son para definir cuando algo es verdadero y falso

#TIPOS DE DATOS COMPUESTOS
listas = [1,2,3,4,"ANDRES","ROJAS", 3.14159 , True , False] #se usa el simbolo [] para indicarle al sistema que se trata de una lista, esta puede contener todos los tipos de datos simples 
# y se separan dichos datos con comas. LA CARACTERISTICA PRINCIPAL DE UNA LISTA ES QUE PERMITE MODIFICAR LOS DATOS QUE ALMACENA
#como se modifica una lista
listas[4] = "pepito" # llamando al nombre de variable de nuestra lista indicandole con el simbolo [] y dentro de el colocando la posicion donde se encuentra el dato que quiero cambiar
# y luego con el = le indico cual es el dato que quiero usar para reemplazar el ya existente

tuplas = (5,6,7,8,"EDUARDO", "GONZALEZ" , 1.43253215 , True , False) #se usa el simbolo () para indicarle al sistema que se trata de una TUPLA, esta puede contener todos los tipos de datos simples 
# y se separan dichos datos con comas. LA CARACTERISTICA PRINCIPAL DE UNA TUPPLA ES QUE NUNCA PERMITE MODIFICAR LOS DATOS QUE ALMACENA

conjunto = {9,10,11,12, "PIPE", "GUTIERREZ" , True , False} #Se usa el simbolo {} para indicarle al sistema que se trata de un CONJUNTO, esta puede contener todos los tipos de datos simples 
# y se separan dichos datos con comas. LA CARACTERISTICA PRINCIPAL DE UN CONJUNTO ES QUE PERMITE MODIFICAR LOS DATOS QUE ALMACENA 
#PERO ESTOS DATOS NO GUARDAN UNA POSICION SI NO QUE STA ES ALEATORIA Y NO SE PUEDEN METER DATOS DUPLICADOS

diccionario = { "institucion" : "SENA" , # en este caso definimos un valor y explicamos al frente que significa ese valor exactamente igual que como un diccionario
               "numero de alumnos" : 452 , # pero en vez de dar una definicion le damos un tipo de dato
               "se pueden agregar booleanos" : True ,
               "tambien decimales" : 6.54235 ,
               "dato duplicado" : "SENA"} # las comas separan los datos del diccionario, cuando acabamos el diccionario  se cierra el corchete {} NO SE PONEN MAS COMAS
               # KEY : VALOR


