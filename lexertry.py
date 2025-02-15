# Función que recorre el string 'code' carácter por carácter y genera una lista de tokens
def tokenize(code):
    tokens = []            # Lista para almacenar los tokens generados
    i = 0                  # Índice para recorrer el string 'code'
    while i < len(code):   # Mientras no se llegue al final del código
        ch = code[i]       # Obtener el carácter actual
        # Si el carácter es un espacio (u otro espacio en blanco), se omite
        if ch.isspace():
            i += 1       # Incrementar el índice para pasar al siguiente carácter
            continue     # Saltar al siguiente ciclo del bucle
        # Si se encuentra el símbolo '#' se debe unir con la palabra siguiente
        if ch == '#':
            token = "#"    # Inicia el token con el símbolo '#'
            i += 1         # Avanza al siguiente carácter
            # Saltar espacios que puedan haber entre '#' y la palabra siguiente
            while i < len(code) and code[i].isspace():
                i += 1
            # Acumular letras, dígitos o guiones bajos para formar el token completo
            while i < len(code) and (code[i].isalnum() or code[i] == '_'):
                token += code[i]  # Añadir el carácter al token
                i += 1            # Avanzar al siguiente carácter
            tokens.append(token)    # Agregar el token formado a la lista de tokens
            continue                # Continuar con la siguiente iteración del bucle
        # Detecta el operador compuesto ":=" revisando dos caracteres juntos
        if ch == ':' and i + 1 < len(code) and code[i+1] == '=':
            tokens.append(":=")  # Agrega el token ":=" a la lista
            i += 2              # Avanza dos posiciones, ya que se han consumido dos caracteres
            continue            # Continuar con la siguiente iteración
        # Si el carácter es uno de los símbolos especiales, se trata como un token individual
        if ch in ['|', '[', ']', ',', '.', ':']:
            tokens.append(ch)   # Agrega el símbolo a la lista de tokens
            i += 1              # Avanza al siguiente carácter
            continue            # Continuar con la siguiente iteración
        # Para cualquier otro caso, se construye un token acumulando caracteres
        token = ""  # Inicializar una cadena vacía para construir el token
        # Acumular caracteres hasta que se encuentre un espacio o un símbolo especial
        while i < len(code) and (not code[i].isspace()) and code[i] not in ['#', '|', '[', ']', ',', '.', ':']:
            token += code[i]  # Añadir el carácter al token
            i += 1            # Avanzar al siguiente carácter
        if token:             # Si se ha construido un token no vacío
            tokens.append(token)  # Agregarlo a la lista de tokens
    return tokens           # Retornar la lista de tokens generada

# Función para procesar declaraciones de variables delimitadas por el símbolo '|'
def parse_variable(tokens, i):
    var_list = []                # Lista para almacenar la declaración de variables
    var_list.append(tokens[i])   # Agregar el token inicial '|' a la lista
    i += 1                       # Avanzar al siguiente token
    # Recorrer y agregar tokens hasta encontrar el token de cierre '|'
    while i < len(tokens) and tokens[i] != '|':
        var_list.append(tokens[i])  # Agregar el token actual a la lista de variables
        i += 1                    # Avanzar al siguiente token
    # Si se encuentra el token de cierre '|', se agrega a la lista
    if i < len(tokens) and tokens[i] == '|':
        var_list.append(tokens[i])  # Agregar el token de cierre
        i += 1                    # Avanzar después del token de cierre
    return var_list, i           # Retornar la lista de variables y la posición actual

# Función para procesar bloques delimitados por '[' y ']'
def parse_block(tokens, i):
    block_list = []              # Lista para almacenar los tokens del bloque
    block_list.append(tokens[i]) # Agregar el token de apertura '['
    i += 1                       # Avanzar al siguiente token después de '['
    # Procesar los tokens que están dentro del bloque hasta encontrar el token de cierre ']'
    while i < len(tokens) and tokens[i] != ']':
        # Si se detecta una declaración de variables dentro del bloque
        if tokens[i] == '|':
            sub, i = parse_variable(tokens, i)  # Procesar la declaración y obtener la sublista
            block_list.append(sub)   # Agregar la sublista de variables al bloque
        # Si se detecta otro bloque anidado dentro del bloque actual
        elif tokens[i] == '[':
            sub, i = parse_block(tokens, i)       # Procesar el bloque anidado recursivamente
            block_list.append(sub)   # Agregar la sublista del bloque anidado
        # Si se detecta un procedimiento anidado dentro del bloque
        elif tokens[i] == 'proc':
            sub, i = parse_proc(tokens, i)        # Procesar el procedimiento anidado
            block_list.append(sub)   # Agregar la sublista del procedimiento
        else:
            block_list.append(tokens[i])  # Agregar el token actual al bloque
            i += 1                        # Avanzar al siguiente token
    # Una vez terminado el contenido del bloque, se agrega el token de cierre ']'
    if i < len(tokens) and tokens[i] == ']':
        block_list.append(tokens[i])  # Agregar el token de cierre ']'
        i += 1                        # Avanzar después del token de cierre
    return block_list, i              # Retornar la lista del bloque y la posición actual

# Función para procesar procedimientos que inician con la palabra 'proc'
def parse_proc(tokens, i):
    proc_list = []                # Lista para almacenar los tokens del procedimiento
    proc_list.append(tokens[i])   # Agregar el token 'proc' a la lista
    i += 1                        # Avanzar al siguiente token
    # Recoger tokens del encabezado del procedimiento hasta encontrar el inicio de un bloque '['
    while i < len(tokens) and tokens[i] != '[':
        proc_list.append(tokens[i])  # Agregar el token del encabezado al procedimiento
        i += 1                    # Avanzar al siguiente token
    # Si se encuentra un bloque, procesarlo de forma recursiva
    if i < len(tokens) and tokens[i] == '[':
        sub, i = parse_block(tokens, i)  # Procesar el bloque asociado al procedimiento
        proc_list.append(sub)    # Agregar la sublista del bloque al procedimiento
    return proc_list, i           # Retornar la lista del procedimiento y la posición actual

# Función para procesar el nivel superior de tokens y agrupar las estructuras encontradas
def parse_top(tokens):
    i = 0                       # Inicializar el índice para recorrer la lista de tokens
    result = []                 # Lista para almacenar las estructuras principales (declaraciones, procs, bloques)
    while i < len(tokens):      # Recorrer todos los tokens
        if tokens[i] == '|':    # Si se detecta el inicio de una declaración de variables
            sub, i = parse_variable(tokens, i)  # Procesar la declaración de variables
            result.append(sub)  # Agregar la sublista resultante a la lista final
        elif tokens[i] == '[':  # Si se detecta el inicio de un bloque
            sub, i = parse_block(tokens, i)     # Procesar el bloque
            result.append(sub)  # Agregar la sublista del bloque a la lista final
        elif tokens[i] == 'proc':  # Si se detecta el inicio de un procedimiento
            sub, i = parse_proc(tokens, i)        # Procesar el procedimiento
            result.append(sub)  # Agregar la sublista del procedimiento a la lista final
        else:
            i += 1             # Si el token no es parte de una estructura especial, se ignora
    return result               # Retornar la lista final con todas las estructuras agrupadas

# Código de entrada: se define un string con el código a procesar
code = """| nom x y one | 
 proc putChips : n andBalloons : m [ 
 |c , b | 
 c := n . 
 b := m . 
 put : c ofType : # chips . put : b ofType : # balloons ] 
 proc goNorth [ 
 while : canMove : 1 inDir : # north do : [ move : 1 InDir : # north . 
]  ] 
 proc goWest [ 
 if : canMove : 1 inDir : # west then : [ move : 1 InDir : # west ] else 
: [ nop .]]
 [ 
 goTo : 3 with : 3 . 
 putChips : 2 andBalloons : 1 . 
 ]"""

# Proceso: tokeniza el código de entrada y luego lo parsea para agrupar las estructuras
tokens = tokenize(code)       # Llama a la función 'tokenize' para convertir el código en una lista de tokens
parsed = parse_top(tokens)      # Llama a 'parse_top' para agrupar los tokens en una estructura anidada

# Imprime la lista final resultante en una sola línea (sin saltos de línea adicionales)
print(parsed, end="")         # Se usa 'end=""' para evitar saltos de línea en la impresión
