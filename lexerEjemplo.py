LPAREN = '[' 
RPAREN = ']'

def lexer(input_string):
    
    
    tokens = []
    palabra = ''
    pila = []

    for char in input_string:
        # TOKENS PARENTESIS
        if char == '[':
            if palabra:
                tokens.append(palabra)
                palabra = ''
            pila.append(tokens)
            tokens = []
            tokens.append(LPAREN) 
        elif char == ']':
            if palabra:
                tokens.append(palabra)
                palabra = ''
            if len(pila) > 0:
                tokens.append(RPAREN)
                sup_token = pila.pop()
                sup_token.append(tokens)
                tokens = sup_token
            else:
                print('Error con los paréntesis, por favor verificar.')
        # PALABRAS
        elif char.isspace():
            if palabra != '':
                tokens.append(palabra)
                palabra = ''
        else:
            palabra += char

    if palabra:
        tokens.append(palabra)

    if len(pila) > 0:
        print('Error con los paréntesis')

    print('TOKENS:', tokens)
    return tokens
