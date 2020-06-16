romanos = {'I':1,
            'V':5, 
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000,
            '': None
            }

def romano_a_entero(numero_romanos):
    if numero_romanos == '':
        return 'Error en formato'
    
    if len(numero_romanos) > 3:   #Solución pasajera
        return 'Error en formato'

    entero = 0
    numRepes = 0
    letraAnt = ''
    for letra in numero_romanos:  #Recorre cada letra del valor/clave introducido
        if letra == letraAnt and numRepes == 3:
            return 'Error formato'
        elif letra == letraAnt:    
            numRepes += 1
        else:
            numRepes = 1
        
        if letra in romanos:  #Si cada letra de la clave que me has introducido están en el diccionario
            entero += romanos[letra]        
        else:
            return 'Error en formato'
            #print('Carácter no válido')
            #entero = ''
            #break
        letraAnt = letra 

    #assert isinstance(entero, int) #Esta herramienta solo se puede poner en desarrollo  #O se cumple o el programa casca
    return entero

