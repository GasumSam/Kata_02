romanos = {'I':1,
            'V':5, 
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000,
            '': None
            }

existen = ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']

def romano_a_entero(numero_romanos):
    if numero_romanos == '':
        return 'Error en formato'
    
    #if len(numero_romanos) > 3:   #Solución pasajera, porque si no me da error cualquier numero mayor de 3 dígitos que meta
       # return 'Error en formato'

    entero = 0
    numRepes = 0
    letraAnt = ''
    #La última operación fue una resta
    fueResta = False  #Es una solución al hecho de que no se pueden tener dos restas seguidas, como es el caso de IXL
    for letra in numero_romanos:  #Recorre cada letra del valor/clave introducido
        
        if letra in romanos:  #Si cada letra de la clave que me has introducido están en el diccionario
            if letraAnt == '' or romanos[letraAnt] >= romanos[letra]:
                entero += romanos[letra]
                fueResta = False 
            else:
                if letraAnt + letra in existen and numRepes < 2 and not fueResta:
                    entero = entero - romanos[letraAnt] * 2 + romanos[letra]
                    fueResta = True
                else:
                    return 'Error en formato'
        
        else:
            return 'Error en formato'

        if letra == letraAnt and numRepes == 3:
            return 'Error formato'
        elif letra == letraAnt:    
            numRepes += 1
        else:
            numRepes = 1
        
        letraAnt = letra

    return entero 
