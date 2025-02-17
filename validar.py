import leer

DVARIABLE="|"
LBLOQUE="["
RBLOQUE="]"
VARIABLES={}
FUNCIONES={}
CONSTANTES=["#chips", "#balloons"]
CONDICIONES=["facing", "canPut", "canPick", "canMove", "canJump"]
INSTRUCCIONES=["goto", "move", "turn", "face", "put", "pick", "move", "jump", "nop"]
SEGUIDOINSTRUCCIONES=["ofType", "inDir", "toThe", "with"]
DIRECCIONES=["#left","#right", "#front", "#back", "around"]
BRUJULA=["#north", "#south", "#west", "#east"]
NUMEROS=[]


# Verificar cada instrucción o cada variable caracter por caracter

def verificar_goto(tokens,i):
    if not(tokens[0] == "goto"):
        return False
    elif not(tokens[1] == ":"):
        return False
    elif not(tokens[2] in NUMEROS):
        return False
    elif not(tokens[3] == "with"):
        return False
    elif not(tokens[4] == ":"):
        return False
    elif not(tokens[5] in NUMEROS):
        return False
    elif not(tokens[6]=="."):
        return False
    else:
        return True

def verificar_move(tokens,i):
    if not(tokens[0] == "move"):
        return False
    elif not(tokens[1] == ":"):
        return False
    elif not(tokens[2] in NUMEROS):
        return False
    elif not(tokens[3] == "."):
        return False
    else:
        return True
    
def verificar_turn(tokens,i):
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
    
def verificar_face(tokens, i):
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

def verificar_putOfType(tokens,i):
    if not(tokens[0] == "put"):
        return False
    elif not(tokens[1] == ":"):
        return False
    elif not(tokens[2] in NUMEROS):
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
    
def verificar_pickOfType(tokens,i):
    if not(tokens[0] == "pick"):
        return False
    elif not(tokens[1] == ":"):
        return False
    elif not(tokens[2] in NUMEROS):
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
    
def verificar_modeToThe(tokens,i):
    if not(tokens[0] == "move"):
        return False
    elif not(tokens[1] == ":"):
        return False
    elif not(tokens[2] in NUMEROS):
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
    
def verificar_moveInDir(tokens,i):
    if not(tokens[0] == "move"):
        return False
    elif not(tokens[1] == ":"):
        return False
    elif not(tokens[2] in NUMEROS):
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
    
def verificar_jumpToThe(tokens,i):
    if not(tokens[0] == "jump"):
        return False
    elif not(tokens[1] == ":"):
        return False
    elif not(tokens[2] in NUMEROS):
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
    
def verificar_jumpInDir(tokens,i):
    if not(tokens[0] == "jump"):
        return False
    elif not(tokens[1] == ":"):
        return False
    elif not(tokens[2] in NUMEROS):
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
    
def verificar_nop(tokens,i):
    if not(tokens[0] == "nop"):
        return False
    elif not(tokens[1] == "."):
        return False
    else:
        return True
    
# Verificar correctamente condiciones

def verificar_facingCondicion(tokens,i):
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
    
def verificar_canPutOfType(tokens,i):
    if not(tokens[0] == "canPut"):
        return False
    elif not(tokens[1] == ":"):
        return False
    elif not(tokens[2] in NUMEROS):
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
    
def verificar_canPickOfType(tokens,i):
    if not(tokens[0] == "canPick"):
        return False
    elif not(tokens[1] == ":"):
        return False
    elif not(tokens[2] in NUMEROS):
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
    
def verificar_canMoveInDir(tokens,i):
    if not(tokens[0] == "canMove"):
        return False
    elif not(tokens[1] == ":"):
        return False
    elif not(tokens[2] in NUMEROS):
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
    
def verificar_canJumpInDir(tokens,i):
    if not(tokens[0] == "canJump"):
        return False
    elif not(tokens[1] == ":"):
        return False
    elif not(tokens[2] in NUMEROS):
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
    
def verificar_canMoveToThe(tokens,i):
    if not(tokens[0] == "canMove"):
        return False
    elif not(tokens[1] == ":"):
        return False
    elif not(tokens[2] in NUMEROS):
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
    
def verificar_canJumpToThe(tokens,i):
    if not(tokens[0] == "canJump"):
        return False
    elif not(tokens[1] == ":"):
        return False
    elif not(tokens[2] in NUMEROS):
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

def verificar_Not(tokens,i):
    if not(tokens[0] == "not"):
        return False
    elif not(tokens[1] == ":"):
        return False
    elif not(tokens[2] in CONDICIONES):
        return False
    else:
        return True

    
    

# Verificación de variables, bloques y procedimientos
def validar_variable(tokens,i):
    print(tokens[0])
    print(tokens[-1])
    if not(tokens[0] in DVARIABLE):
        return False
    elif not(tokens[-1] in DVARIABLE):
        return False
    elif not(tokens[1][0].islower()):
        return False
    elif not(tokens[4][0].islower()):
        return False
    else:
        return True
    
def validar_bloque(tokens, i):
    if not(tokens[0] in LBLOQUE) and not(tokens[-1] in RBLOQUE):
        return False
    else:
        return True

def validar_procedimiento(tokens, i):
    return True
    
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
        
