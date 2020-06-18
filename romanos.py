'''
romanos = {'I':1,
            'V':5, 
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000,
            '': None
            }
'''
romanos = {'M':1000, 'CM':900, 'D':500, 'CD':400, 'C':100, 'XC':90, 'L':50, 'XL':40, 'X':10, 'IX':9, 'V':5, 'IV':4, 'I':1,}

#existen = ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']

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
                if letraAnt + letra in romanos.keys() and numRepes < 2 and not fueResta:
                    entero = entero - romanos[letraAnt] * 2 + romanos[letra]
                    fueResta = True
                else:
                    return 'Error en formato'
        
        else:
            return 'Error en formato'

        if letra == letraAnt and numRepes == 3:
            return 'Error en formato'
        elif letra == letraAnt:    
            numRepes += 1
        else:
            numRepes = 1
        
        letraAnt = letra

    return entero 

def entero_a_romano(valor):
    if valor > 3999:
        return 'Overflow'  #Con esta orden validamos la línea 79 del test para que no de error

    componentes = descomponer(valor)

    res = ''
    for valor in componentes:
        while valor > 0:
            k, v = busca_valor_menor_o_igual(valor)
            valor -= v
            res += k

    return res

def busca_valor_menor_o_igual(v):
    for key, value in romanos.items():
        if value <= v:
            return key, value

def descomponer(numero):
    res = []
    for orden in range(3, 0, -1):
        resto = numero % 10 ** orden
        res.append(numero - resto)
        numero = resto
    res.append(numero)
    return res