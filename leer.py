# ALejandro Hoyos 202215277 - Emmanuel Blanco 202312743

# Debemos decir si el programa corresponde al lenguaje del robot o no

# Pasos:
# 1) Leer archivo linea por linea
# 2) Revisar que cada linea cumpla con una estructura válida
# 3) Llevar un registro de las variables y procedimientos definidos ya sea que esten dentro de un bloque de [] 
# 4) Si se llega a encontrar un error se debe lanzar una excepción buscando el error

# Para el caso de ser válido lo mpas importante:
# 1) Las variables deben declararse antes de ser usadas
# 2) Los procedimientos deben definirse antes de ser usados o llamados
# 3) Cada línea de código o de texto debe seguir el formato correcto según el lenguaje del robot


"""
# Esta función se encarga de leer el archivo linea por linea y acto seguido leer caracter por caracter para separar cada simbolo, palabra, etc...
# en una lista que en general contiene todos los simbolos y palabras necesarios si ve un un simbolo de declaración de variable lo separa
# de cualquier palabra y así para los demás simbolos con excepción de la asignación de variable ":=" 

# Retorna una lista con las diferentes simbolos palabras y demás 
# Ejemplo = ['|', 'nom', 'x', 'y', 'one', '|']

"""
def lexer(nombreArchivo):
    archivo = open (nombreArchivo , 'r' ) # Se lee el archivo de texto
    
    lineas=archivo.readlines() # Se guarda en una lista de listas
    
    tokens=[] 
    
    palabra="" # Se guarda la palabra cuando se revisa char por char

    for linea in lineas: # Recorre cada linea del archivo

        for caracter in linea: # Revisar cada caracter en una linea

            if caracter=="|":
                if palabra!= "":
                    tokens.append(palabra)
                    palabra=""
                tokens.append(caracter)

            elif caracter=="[":
                if palabra!= "":
                    tokens.append(palabra)
                    palabra=""
                tokens.append(caracter)
            
            elif caracter=="]":
                if palabra!= "":
                    tokens.append(palabra)
                    palabra=""
                tokens.append(caracter)

            elif caracter==".":
                if palabra!= "":
                    tokens.append(palabra)
                    palabra=""
                tokens.append(caracter)

            elif caracter==":":
                if palabra!= "":
                    tokens.append(palabra)
                    palabra=""
                tokens.append(caracter)

            elif caracter=="=" and tokens[-1]==":":
                if palabra!= "":
                    tokens.append(palabra)
                    palabra=""
                del tokens[-1]
                tokens.append(":=")
            
            elif caracter==",":
                if palabra!= "":
                    tokens.append(palabra)
                    palabra=""
                tokens.append(caracter)

            elif caracter.isspace():
                if palabra!= "":
                    tokens.append(palabra)
                    palabra=""

            else: palabra+=caracter
    archivo.close()
    return tokens



"""
Esta función se encarga de crear listas por cada declaración de variables que encuentre en el código tal como sea el caso 
dentro de un procedimiento o dentro de un bloque de código, si encuentre dos simbolos de definición de variable los agrega como una lista
"""
def variable(tokens,i):
    listavar=[]
    listavar.append(tokens[i])
    indice=i+1
    while indice < len(tokens) and tokens[indice] !="|":
        listavar.append(tokens[indice])
        indice+=1
    if indice < len(tokens) and tokens[indice] =="|":
        listavar.append(tokens[indice])
        indice+=1
    return listavar, indice 





"""
Esta función se encarga de crear listas por cada bloque que ha sido pasado por parametro en el código del robot, ya sea 
en el interior de un procedimiento o por fuera del procedimiento. Este método utiliza recursión para saber si dentro del 
bloque de ejecución existe otro bloque de ejecución"
"""

def bloque(tokens,i):
    listabloque=[]
    listabloque.append(tokens[i])
    indice=i+1
    while indice < len(tokens) and tokens[indice] != "]":
        if tokens[indice]=="|":
            listavariable, indice = variable(tokens,indice)
            listabloque.append(listavariable)
        elif tokens[indice] =="[":
            sub, indice = bloque(tokens, indice) 
            listabloque.append(sub)
        elif tokens[indice] == "proc":
            listaprocedimiento, indice = procedimiento(tokens, indice)
            listabloque.append(listaprocedimiento)
        else: 
            listabloque.append(tokens[indice])
            indice+=1
        
    if indice < len(tokens) and tokens[indice] =="]":
        listabloque.append(tokens[indice])
        indice+=1
    
    return listabloque, indice





"""
Esta función se encarga de crear listas por cada uno de los procedimientos encontrados en el código 
y si encuentra bloques o declaración de variables dentro de su
estructura, llamará a la función ya sea de bloque o de vaiable para obtener cada lista dentro de la lista general de procedimiento
"""

def procedimiento(tokens,i):
    listaprocedimiento=[]
    listaprocedimiento.append(tokens[i])
    indice=i+1
    while indice < len(tokens) and tokens[indice] != "[":
        listaprocedimiento.append(tokens[indice])
        indice+=1
    
    if indice < len(tokens) and tokens[indice] == "[":
        listabloque, indice = bloque(tokens, indice)
        listaprocedimiento.append(listabloque)
    
    return listaprocedimiento, indice




"""
Esta función es la encargada de retornar una lista separada por cada estructura principal del código ya sea una lista 
para declaración de variables, una lista para procedimientos, una lista para bloques, si encuentra que hay un bloque dentro de un
procedimiento lo guarda como una lista sobre la lista de procedimiento con sus debido carácteres. Se recorre la lista que retorna
los simbolos y palabras por separado y según su indice se envía a las otras funciones, estas retornan la lista y el indice 
para seguir con la ejecución sin necesidad de repetir el indice ya revisado

Retorna: Lista con listas de procedimiento, declaración de variables o bloques

Ejemplo: [['|', 'nom', 'x', 'y', 'one', '|'],['proc', 'goNorth', ['[', 'while', ':', 'canMove', ':', '1', 'inDir', ':',
 '#north', 'do', ':', ['[', 'move', ':', '1', 'InDir', ':', '#north', '.', ']'], ']']]]

"""
def resultado(tokens):
    i=0
    total=[]
    while i < len(tokens):
        if tokens[i] == "|":
            listavariable, i = variable(tokens , i)
            total.append(listavariable)
        elif tokens[i] == "[":
            listabloque, i = bloque(tokens,i)
            total.append(listabloque)
        elif tokens[i] == "proc":
            listaprocedimiento, i = procedimiento(tokens, i)
            total.append(listaprocedimiento)
        else:
            i+=1
    return total