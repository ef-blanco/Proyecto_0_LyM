LPAREN = '[' 
RPAREN = ']'

def lexer(input_string):
    
    
    tokens = []
    palabra = ''

    for char in input_string:
        # TOKENS PARENTESIS
        
        # PALABRAS
        if char.isspace():
            if palabra != '':
                tokens.append(palabra)
                palabra = ''
        else:
            palabra += char

    if palabra:
        tokens.append(palabra)

    if len(tokens) > 0:
        print('TOKENS:', tokens)
    
    return tokens

def prueba (archivo): #Este método devuelve un solo string con todas las lineas de codigo
    
    archivo = open (archivo , 'r' )
    
    lineas=archivo.readlines() # Devuelvele una lista con todas las lineas de que tiene el archivo
    
    string_con_codigo = ""
    
    for linea in lineas:
        lin_cod = lexer(linea)
        if len(lin_cod)>0:
            string_con_codigo+=" ".join(lin_cod)
            
    print(string_con_codigo)
        
prueba("prueba.txt")
