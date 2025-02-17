# Alejandro Hoyos - Proyecto 0 - Lexer para Robot

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

# Después de tutoria: 
# TODO Implementar lexer para leer archivo por archivo mirando correctamente cómo funciona mediante tokes y pilas para agregar correctamente el que sea
# TODO Revisar video de implementación de un lexer sin librería y cómo debería ser lo correcto para analizarlo
# TODO utilizar ChatGPT para obtener información de como debería implementar el lexer 
# TODO ver videos para ver un analizador léxico de cómo implementar dicho lexer

# EJEMPLO:
# int score = 10;
# [KEYWORD("int"), ID("score"), OP_ASSIGN:("="), INTEGER("10"), SEMICOLON(";")]


def lexer(nombreArchivo):
    archivo = open (nombreArchivo , 'r' )
    
    lineas=archivo.readlines() 
    
    tokens=[] 
    
    palabra="" 

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

# tokens=lexer("prueba.txt")
# print(tokens)

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
        else: # TODO potencial error
            listabloque.append(tokens[indice])
            indice+=1
        
    if indice < len(tokens) and tokens[indice] =="]":
        listabloque.append(tokens[indice])
        indice+=1
    
    return listabloque, indice

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

# lexer= resultado(tokens)
# print(lexer)


    # Mover linea: ALT + FLECHA
    # Duplicar linea: ALT + SHIFT + FLECHA
    # Borrar palabra: CTRL + DELETE
    # Borrar linea de código: CTRL + SHIFT + K
    # Seleccionar linea entera: CTRL + L
    # Seleccionar apariciones de palabras: CTRL + SHIFT + L
    # Comentar o descomentar: CTRL + c CEBILLA
    # Desplazar entre lineas: CTRL + FLECHAS
    # Seleccionar entre lineas palabras y demás: CTRL + SHIFT + FLECHA
    # Ejecutar terminal o consola con F5 o CTRL + F5
    # "psvm" para haecr el método de main
    # "sout" para obtener el método System.out.println()