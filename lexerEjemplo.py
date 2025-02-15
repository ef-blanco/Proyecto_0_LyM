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
    
    archivo = open (archivo ,'r')
    
    lineas=archivo.readlines() # Devuelvele una lista con todas las lineas de que tiene el archivo
    
    lista_con_codigo = []
    
    for linea in lineas:
        lin_cod = lexer(linea)
        if len(lin_cod)>0:
            lista_con_codigo.append(lin_cod)
            
    print("lista_cod: ",lista_con_codigo)
    
    definicion_var = [] #Esta lista contendra las lista que contengan el caracter '|', que seran los casos vinculados a la declaracion de variables
    
    procedimientos = [] #Esta lista contendra las listas que contengan el string 'proc', que seran los casos de procedimientos
    
    bloques = [] #Esta lista contendra las listas que contengan los carateres '['']' y que no contengan los caracteres de los otros casos
    
    #Se unen los ']' que estan solos en una linea a la linea anterior
    
    listas_con_solo_corcheteR = [] #Corregido
    l = 0
    while l<len(lista_con_codigo):
        if (len(lista_con_codigo[l]) == 1)and(lista_con_codigo[l][0]=="]"):
            listas_con_solo_corcheteR.append(l)
        l+=1
                   
    for i in listas_con_solo_corcheteR:

        if lista_con_codigo[i-1] != ["]"]:
            lista_con_codigo[i-1].extend(lista_con_codigo[i])
        else:
            k = 1
            stop = False
            while ((i-k)>0)and(not stop):
                if lista_con_codigo[i-k] != ["]"]:
                    stop =True
                    lista_con_codigo[i-k].extend(lista_con_codigo[i])
                k+=1
               
    elementos_borrar = len(listas_con_solo_corcheteR)
    while elementos_borrar>0:
        lista_con_codigo.remove(["]"])
        elementos_borrar-=1
        
    
    #Se unen todas las lineas que conforman un procedimiento
    listas_con_proc = [] #Esta lista contendra la posicion de las lista con 'proc'
    
    l = 0
    while l<len(lista_con_codigo):
        if 'proc' in lista_con_codigo[l]:
            listas_con_proc.append(l)
        l+=1
        
    #for lista in lista_con_codigo:
        #if 'proc' in lista:
            #listas_con_proc.append(lista_con_codigo.index(lista))
    
    elementos_borrar = [] #Esta lista indica que elementos se eliminaran luego de juntar todas las lineas de un procedimiento
    
    for i in listas_con_proc:
        j = i
        corchete_detectado = False
        nuevalista = []
        
        while (j<len(lista_con_codigo))and(not corchete_detectado):
            
            if ']' in lista_con_codigo[j]: #Este ciclo junta todas las listas que hacen parte de un solo procedimiento
                corchete_detectado = True #Aun es necesario incluir el caso en el que hay subbloques dentro de un proc, el ciclo se detendría al ver el primer ']'
                
            elementos_borrar.append(lista_con_codigo[j])
            nuevalista.extend(lista_con_codigo[j])
            j+=1
        
        lista_con_codigo.insert(i,nuevalista) #Inserta en la lista el procedimiento en la pos de la linea en la que se empezo
        
    for elem in elementos_borrar: #Se eliminan las listas que fueron juntadas con otras
        lista_con_codigo.remove(elem)
    
    
    #CORREGIR
    #Se unen los '[' que se encuentran solo en una linea a la linea siguiente
    
    listas_con_solo_corcheteL = [] #Lista con indices de Listas con solo "["
    
    l = 0
    while l<len(lista_con_codigo):
        if (len(lista_con_codigo[l])==1)and(lista_con_codigo[l][0]=='['):
            listas_con_solo_corcheteR.append(l)
        l+=1
        
    #for lista in lista_con_codigo:
        #if (len(lista) == 1)and(lista[0]=="["):
            #listas_con_solo_corcheteR.append(lista_con_codigo.index(lista))
            
    elementos_borrar = [] #Esta lista indica que elementos se eliminaran luego de juntar todos los '[' solos con su linea siguiente
    
    for i in listas_con_solo_corcheteL:
        nueva_lista = lista_con_codigo[i][:] #Se copia el '[' en nueva_lista
        nueva_lista.extend(lista_con_codigo[i+1]) #Se le añade a la lista lo que estaba en la linea siguiente
        elementos_borrar.append(lista_con_codigo[i])
        elementos_borrar.append(lista_con_codigo[i+1])
        lista_con_codigo.insert(i,nueva_lista) #Se añade la nueva lista a la posicion donde estaba la linea antes del ']'
    
    for elem in elementos_borrar: #Se eliminan las listas que fueron juntadas con otras
        lista_con_codigo.remove(elem)
        
    print("CONTENIDO: ",lista_con_codigo)        
    
    for lista in lista_con_codigo:
        if 'proc' in lista:
            procedimientos.append(lista)
        elif '|' in lista:
            definicion_var.append(lista)
    
    
    print("DEF_VAR: ",definicion_var)
    print("PROCS: ",procedimientos)
        
prueba("prueba.txt")
