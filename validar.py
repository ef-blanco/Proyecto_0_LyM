import leer

DVARIABLE="|"
LBLOQUE="["
RBLOQUE="]"
VARIABLES={}
NOMBRES_VARIABLES = [] #Lista con los nombres de las variables
FUNCIONES={}
CONSTANTES=["#chips", "#balloons"]
CONDICIONES=["facing", "canPut", "canPick", "canMove", "canJump"]
INSTRUCCIONES=["goto", "move", "turn", "face", "put", "pick", "move", "jump", "nop"]
SEGUIDOINSTRUCCIONES=["ofType", "inDir", "toThe", "with"]
DIRECCIONES=["#left","#right", "#front", "#back", "around"]
BRUJULA=["#north", "#south", "#west", "#east"]
NUMEROS=[]
PALABRAS_RESERVADAS = ["|","[","]","#chips", "#balloons","facing", "canPut", "canPick", "canMove", "canJump",
                       "goto", "move","turn", "face", "put", "pick", "move", "jump", "nop","ofType", "inDir",
                       "toThe", "with","#left","#right", "#front", "#back", "around", "#north", "#south", "#west", "#east"]


# Verificar cada instrucción o cada variable caracter por caracter

def verificar_goto(tokens,i)->bool:
    if not(tokens[0] == "goto"):
        return False
    elif not(tokens[1] == ":"):
        return False
    elif not((tokens[2] in NUMEROS)or(tokens[2] in NOMBRES_VARIABLES)): #Cambio:Se verifica que el valor también pueda estar en una variable
        return False
    elif not(tokens[3] == "with"):
        return False
    elif not(tokens[4] == ":"):
        return False
    elif not((tokens[5] in NUMEROS)or(tokens[5] in NOMBRES_VARIABLES)): #Cambio:Se verifica que el valor también pueda estar en una variable
        return False
    elif not(tokens[6]=="."):
        return False
    else:
        return True

def verificar_move(tokens,i)->bool:
    if not(tokens[0] == "move"):
        return False
    elif not(tokens[1] == ":"):
        return False
    elif not((tokens[2] in NUMEROS)or(tokens[2] in NOMBRES_VARIABLES)): #Cambio:Se verifica que el valor también pueda estar en una variable
        return False
    elif not(tokens[3] == "."):
        return False
    else:
        return True
    
def verificar_turn(tokens,i)->bool:
    if not(tokens[0] == "turn"):
        return False
    elif not(tokens[1] == ":"):
        return False
    elif not(tokens[2] in DIRECCIONES):
        return False
    elif not(tokens[3] == "."):
        return False
    else:
        return True
    
def verificar_face(tokens, i)->bool:
    if not(tokens[0] == "face"):
        return False
    elif not(tokens[1] == ":"):
        return False
    elif not(tokens[2] in BRUJULA):
        return False
    elif not(tokens[3] == "."):
        return False
    else:
        return True

def verificar_putOfType(tokens,i)->bool:
    if not(tokens[0] == "put"):
        return False
    elif not(tokens[1] == ":"):
        return False
    elif not((tokens[2] in NUMEROS)or(tokens[2] in NOMBRES_VARIABLES)): #Cambio:Se verifica que el valor también pueda estar en una variable
        return False
    elif not(tokens[3] == "ofType"):
        return False
    elif not(tokens[4] == ":"):
        return False
    elif not(tokens[5] in CONSTANTES):
        return False
    elif not(tokens[6]=="."):
        return False
    else:
        return True
    
def verificar_pickOfType(tokens,i)->bool:
    if not(tokens[0] == "pick"):
        return False
    elif not(tokens[1] == ":"):
        return False
    elif not((tokens[2] in NUMEROS)or(tokens[2] in NOMBRES_VARIABLES)): #Cambio:Se verifica que el valor también pueda estar en una variable
        return False
    elif not(tokens[3] == "ofType"):
        return False
    elif not(tokens[4] == ":"):
        return False
    elif not(tokens[5] in CONSTANTES):
        return False
    elif not(tokens[6]=="."):
        return False
    else:
        return True
    
def verificar_moveToThe(tokens,i)->bool: #Cambio: el nombre de la función era modeToThe
    if not(tokens[0] == "move"):
        return False
    elif not(tokens[1] == ":"):
        return False
    elif not((tokens[2] in NUMEROS)or(tokens[2] in NOMBRES_VARIABLES)): #Cambio:Se verifica que el valor también pueda estar en una variable
        return False
    elif not(tokens[3] == "toThe"):
        return False
    elif not(tokens[4] == ":"):
        return False
    elif not(tokens[5] in DIRECCIONES):
        return False
    elif not(tokens[6]=="."):
        return False
    else:
        return True
    
def verificar_moveInDir(tokens,i)->bool:
    if not(tokens[0] == "move"):
        return False
    elif not(tokens[1] == ":"):
        return False
    elif not((tokens[2] in NUMEROS)or(tokens[2] in NOMBRES_VARIABLES)): #Cambio:Se verifica que el valor también pueda estar en una variable
        return False
    elif not(tokens[3] == "inDir"):
        return False
    elif not(tokens[4] == ":"):
        return False
    elif not(tokens[5] in BRUJULA):
        return False
    elif not(tokens[6]=="."):
        return False
    else:
        return True
    
def verificar_jumpToThe(tokens,i)->bool:
    if not(tokens[0] == "jump"):
        return False
    elif not(tokens[1] == ":"):
        return False
    elif not((tokens[2] in NUMEROS)or(tokens[2] in NOMBRES_VARIABLES)): #Cambio:Se verifica que el valor también pueda estar en una variable
        return False
    elif not(tokens[3] == "inDir"):
        return False
    elif not(tokens[4] == ":"):
        return False
    elif not(tokens[5] in DIRECCIONES):
        return False
    elif not(tokens[6]=="."):
        return False
    else:
        return True
    
def verificar_jumpInDir(tokens,i)->bool:
    if not(tokens[0] == "jump"):
        return False
    elif not(tokens[1] == ":"):
        return False
    elif not((tokens[2] in NUMEROS)or(tokens[2] in NOMBRES_VARIABLES)): #Cambio:Se verifica que el valor también pueda estar en una variable
        return False
    elif not(tokens[3] == "inDir"):
        return False
    elif not(tokens[4] == ":"):
        return False
    elif not(tokens[5] in BRUJULA):
        return False
    elif not(tokens[6]=="."):
        return False
    else:
        return True
    
def verificar_nop(tokens,i)->bool:
    if not(tokens[0] == "nop"):
        return False
    elif not(tokens[1] == "."):
        return False
    else:
        return True
    
# Verificar correctamente condiciones

def verificar_facingCondicion(tokens,i)->bool:
    if not(tokens[0] == "facing"):
        return False
    elif not(tokens[1] == ":"):
        return False
    elif not(tokens[2] in BRUJULA):
        return False
    elif not(tokens[3] == "."):
        return False
    else:
        return True
    
def verificar_canPutOfType(tokens,i)->bool:
    if not(tokens[0] == "canPut"):
        return False
    elif not(tokens[1] == ":"):
        return False
    elif not((tokens[2] in NUMEROS)or(tokens[2] in NOMBRES_VARIABLES)): #Cambio:Se verifica que el valor también pueda estar en una variable
        return False
    elif not(tokens[3] == "ofType"):
        return False
    elif not(tokens[4] == ":"):
        return False
    elif not(tokens[5] in CONSTANTES):
        return False
    elif not(tokens[6]=="."):
        return False
    else:
        return True
    
def verificar_canPickOfType(tokens,i)->bool:
    if not(tokens[0] == "canPick"):
        return False
    elif not(tokens[1] == ":"):
        return False
    elif not((tokens[2] in NUMEROS)or(tokens[2] in NOMBRES_VARIABLES)): #Cambio:Se verifica que el valor también pueda estar en una variable
        return False
    elif not(tokens[3] == "ofType"):
        return False
    elif not(tokens[4] == ":"):
        return False
    elif not(tokens[5] in CONSTANTES):
        return False
    elif not(tokens[6]=="."):
        return False
    else:
        return True
    
def verificar_canMoveInDir(tokens,i)->bool:
    if not(tokens[0] == "canMove"):
        return False
    elif not(tokens[1] == ":"):
        return False
    elif not((tokens[2] in NUMEROS)or(tokens[2] in NOMBRES_VARIABLES)): #Cambio:Se verifica que el valor también pueda estar en una variable
        return False
    elif not(tokens[3] == "inDir"):
        return False
    elif not(tokens[4] == ":"):
        return False
    elif not(tokens[5] in BRUJULA):
        return False
    elif not(tokens[6]=="."):
        return False
    else:
        return True
    
def verificar_canJumpInDir(tokens,i)->bool:
    if not(tokens[0] == "canJump"):
        return False
    elif not(tokens[1] == ":"):
        return False
    elif not((tokens[2] in NUMEROS)or(tokens[2] in NOMBRES_VARIABLES)): #Cambio:Se verifica que el valor también pueda estar en una variable
        return False
    elif not(tokens[3] == "inDir"):
        return False
    elif not(tokens[4] == ":"):
        return False
    elif not(tokens[5] in BRUJULA):
        return False
    elif not(tokens[6]=="."):
        return False
    else:
        return True
    
def verificar_canMoveToThe(tokens,i)->bool:
    if not(tokens[0] == "canMove"):
        return False
    elif not(tokens[1] == ":"):
        return False
    elif not((tokens[2] in NUMEROS)or(tokens[2] in NOMBRES_VARIABLES)): #Cambio:Se verifica que el valor también pueda estar en una variable
        return False
    elif not(tokens[3] == "toThe"):
        return False
    elif not(tokens[4] == ":"):
        return False
    elif not(tokens[5] in DIRECCIONES):
        return False
    elif not(tokens[6]=="."):
        return False
    else:
        return True
    
def verificar_canJumpToThe(tokens,i)->bool:
    if not(tokens[0] == "canJump"):
        return False
    elif not(tokens[1] == ":"):
        return False
    elif not((tokens[2] in NUMEROS)or(tokens[2] in NOMBRES_VARIABLES)): #Cambio:Se verifica que el valor también pueda estar en una variable
        return False
    elif not(tokens[3] == "toThe"):
        return False
    elif not(tokens[4] == ":"):
        return False
    elif not(tokens[5] in DIRECCIONES):
        return False
    elif not(tokens[6]=="."):
        return False
    else:
        return True

def verificar_Not(tokens,i)->bool:
    if not(tokens[0] == "not"):
        return False
    elif not(tokens[1] == ":"):
        return False
    elif not(tokens[2] in CONDICIONES):
        return False
    else:
        return True

    
    

# Verificación de variables, bloques y procedimientos

def validar_variable(lista,i)->bool:
    if not(lista[0] in DVARIABLE):
        return False
    elif not(lista[-1] in DVARIABLE):
        return False
    j=1
    while j < len(lista) -1:
        print(lista[j])
        if lista[j] != ",":
            if not(lista[j][0].islower()): #Falta verificar que la palabra no sea reservada
                return False
        elif lista[j] ==",":
            j+=1
            continue
        else:
            return False
        j+=1
    else:
        return True 
    
def validar_bloque(tokens, i)->bool:
    resultado = True
    if not(tokens[0] in LBLOQUE) or not(tokens[-1] in RBLOQUE):
        return False
    
    lista_instrucciones = [] #Tendra en listas las intrucciones a revisar
    validacion_instrucciones = True
    punto_detectado = False
    j=1
    while j < len(tokens)-1: #La condicion tal vez deba ser j < len(tokens)-2
        if isinstance(tokens[j],list):
            if tokens[j][0]=="|":
                resultado = validar_variable(tokens[j], j) and resultado
            
            elif (tokens[j][0] == "[")and(tokens[j][-1] == "]"):
                resultado = resultado and validar_bloque(tokens[j],j)
        
        
        else:
            nueva_instruc = []
            nueva_instruc.append(tokens[j])
            if tokens == ".":
                punto_detectado = True
                
            if punto_detectado: #Si se detecta un punto significa que ya termino una instruccion
                lista_instrucciones.append(nueva_instruc) #La instruccion se añade a la lista de instrucciones
                nueva_instruc = []
                punto_detectado = False
            
        j+=1
        
        instruc_Tipo = {} #Guarda indice_insturccion (llave): tipo (valor)
        for instruc in lista_instrucciones:
            if ":=" in instruc:
                instruc_Tipo[lista_instrucciones.index(instruc)] = "ASIGNACION"
            
            elif "goto" in instruc:
                instruc_Tipo[lista_instrucciones.index(instruc)] = "GOTO"
            
            elif "move" in instruc:
                instruc_Tipo[lista_instrucciones.index(instruc)] = "MOVE"
                
            elif "turn" in instruc:
                instruc_Tipo[lista_instrucciones.index(instruc)] = "TURN"
                
            elif "face" in instruc:
                instruc_Tipo[lista_instrucciones.index(instruc)] = "FACE"
            
            elif ("put" in instruc) and ("ofType" in instruc):
                instruc_Tipo[lista_instrucciones.index(instruc)] = "PUT_OFTYPE"
            
            elif ("pick" in instruc) and ("ofType" in instruc):
                instruc_Tipo[lista_instrucciones.index(instruc)] = "PICK_OFTYPE"
            
            elif ("move" in instruc) and ("toThe" in instruc):
                instruc_Tipo[lista_instrucciones.index(instruc)] = "MOVE_TOTHE"
            
            elif ("move" in instruc) and ("inDir" in instruc):
                instruc_Tipo[lista_instrucciones.index(instruc)] = "MOVE_INDIR"
            
            elif ("jump" in instruc) and ("toThe" in instruc):
                instruc_Tipo[lista_instrucciones.index(instruc)] = "JUMP_TOTHE"
            
            elif ("jump" in instruc) and ("inDir" in instruc):
                instruc_Tipo[lista_instrucciones.index(instruc)] = "JUMP_INDIR"
            
            elif "nop" in instruc:
                instruc_Tipo[lista_instrucciones.index(instruc)] = "NOP"
            
            
            for indice in instruc_Tipo.keys(): #Se revisa cada instruccion y se va modificando un booleano que determina si todas las instrucciones fueron correctas
                tipo = instruc_Tipo[indice]
                match tipo:
                    case "ASIGNACION":
                        validacion_instrucciones = validacion_instrucciones and verificarAsignacion
                        
                    case "GOTO":
                        validacion_instrucciones = validacion_instrucciones and verificar_goto(lista_instrucciones[indice],indice)
                        
                    case "MOVE":
                        validacion_instrucciones = validacion_instrucciones and verificar_move(lista_instrucciones[indice],indice)
                        
                    case "TURN":
                        validacion_instrucciones = validacion_instrucciones and verificar_turn(lista_instrucciones[indice],indice)
                        
                    case "FACE":
                        validacion_instrucciones = validacion_instrucciones and verificar_face(lista_instrucciones[indice],indice)
                        
                    case "PUT_OFTYPE":
                        validacion_instrucciones = validacion_instrucciones and verificar_canPutOfType(lista_instrucciones[indice],indice)
                    
                    case "PICK_OFTYPE":
                        validacion_instrucciones = validacion_instrucciones and verificar_canPickOfType(lista_instrucciones[indice],indice)
                    
                    case "MOVE_TOTHE":
                        validacion_instrucciones = validacion_instrucciones and verificar_canMoveToThe(lista_instrucciones[indice],indice)
                        
                    case "MOVE_INDIR":
                        validacion_instrucciones = validacion_instrucciones and verificar_moveInDir(lista_instrucciones[indice],indice)
                    
                    case "JUMP_TOTHE":
                        validacion_instrucciones = validacion_instrucciones and verificar_jumpToThe(lista_instrucciones[indice],indice)
                    
                    case "JUMP_INDIR":
                        validacion_instrucciones = validacion_instrucciones and verificar_jumpInDir(lista_instrucciones[indice],indice)
                        
                    case "NOP":
                        validacion_instrucciones = validacion_instrucciones and verificar_nop(lista_instrucciones[indice],indice)
                
    return validacion_instrucciones and resultado
                    
            
            
    
    
    

def validar_procedimiento(tokens, i)->bool:
    result = True
    if not(tokens[0] == "proc"):
        result = False
    
    elif not(tokens[1] in PALABRAS_RESERVADAS): #Revisa que el nombre del proc no esté dentor de las palabras reservadas
        result = False
    
    parametros = 0 #Lleva el conteo de cuantos parametros tiene el procedimiento
    if tokens[2] == ":": #Si llega a haber un parametro...
        parametros+=1
        if not((tokens[3] in NUMEROS)or(tokens[3] in NOMBRES_VARIABLES)): #Se espera que el parametro se un numero o variable
            result = False
        
        if tokens[4]=="and": #Si llega a haber otro parametro...
            parametros+=1
            if not(tokens[5] == ":"): #Deben haber : despues del and
                result = False
            if not((tokens[6] in NUMEROS)or(tokens[6] in NOMBRES_VARIABLES)): #Se espera que el parametro se un numero o variable
                result = False
    
    pos_actual = 2          
    if parametros>0: #Estos condicionales ayudan a recuperar la posicion en la que esta independiente de si hubieron parametros o no
        if parametros == 1:
            pos_actual = 4
        else:
            pos_actual = 7
            
    verificacionBloque = True #El bloque del procedimiento tendra que ser revisado por validar_procedimiento
    if isinstance(tokens[pos_actual],list): #Revise si en las posicion de la lista del proc se tiene una lista
        verificacionBloque = validar_bloque(tokens[pos_actual],i) #Manda al bloque a revision
    else:
        result = False
    
    result = result and verificacionBloque #Se valida que el procedimiento esta bien si su bloque tambien lo esta
        
    return result
    
def validar(tokens):
    i=0
    while i < len(tokens):
        
        j=0
        while j < len(tokens[i]):

            if tokens[i][j]=="|":
                resultado=validar_variable(tokens[i], j)
                j=len(tokens[i])

            elif tokens[i][j]=="[":
                resultado=validar_bloque(tokens[i], j)
                j=len(tokens[i])

            elif tokens[i][j]=="proc":
                resultado=validar_procedimiento(tokens[i], j)
                j=len(tokens[i])

            else:
                continue
        i+=1
    return resultado

lista=leer.lexer("pruebaVariables.txt")
print(lista)
arroas=leer.resultado(lista)
print(arroas)

respuesta=validar(arroas)
print(respuesta)
        
