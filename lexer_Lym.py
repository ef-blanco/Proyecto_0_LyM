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

DVARIA="|"
LBLOQUE="["
RBLOQUE="]"
PROC="proc"

def lexer(nombreArchivo):
    archivo = open (nombreArchivo , 'r' )
    
    lineas=archivo.readlines() # Devuelvele una lista con todas las lineas de que tiene el archivo
    
    tokens=[] # Es la lista temporal en la cual se guardan los casos del lenguaje: PROC, VARIABLES, BLOQUES
    
    palabra="" # Se guardan las palabras necesarias para cada caso 
    
    listaTotal=[] # Indica una lista de listas que incluye cada caso donde existe un proceso principal
    
    anteriorVar=False # Indica si ya hay una decalración de variables antes

    for linea in lineas: # Recorre cada linea del archivo

        for caracter in linea: # Revisar cada caracter en una linea

            # Primer caso declaración de variables
            if caracter in DVARIA:
                if palabra:
                    tokens.append(palabra)
                    palabra=""

                if anteriorVar==False:
                    if len(tokens)>0:
                        listaTotal.append(tokens)
                        tokens=[]
                    if len(tokens)==0:
                        tokens.append(caracter)
                        anteriorVar=True

                elif anteriorVar==True:
                    tokens.append(caracter)
                    listaTotal.append(tokens)
                    anteriorVar=False
                    tokens=[]

                


            # Caso para espacios
            elif caracter.isspace():
                if palabra!= "":
                    print("PALABRAS: ",palabra)
                    tokens.append(palabra)
                    palabra=""

            else: palabra+=caracter
        

    print("TOKENS: ",tokens)
    print("PALABRAS: ",palabra)
    print("CONTENIDO: ",listaTotal)
    archivo.close()

lexer("prueba.txt")


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