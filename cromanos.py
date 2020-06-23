class RomanNumber():
    __symbols = {'M':1000, 'CM':900, 'D':500, 'CD':400, 'C':100, 'XC':90, 'L':50, 'XL':40, 'X':10, 'IX':9, 'V':5, 'IV':4, 'I':1,}

    def __init__(self, valor):                                      #    def __init__(self, 'XXIV'):  - Entra el valor XXIV
        if isinstance(valor, str): #Si valor es una cadena    /  #if isinstance(valor, str):
            self.value = self.romano_a_entero(valor)                #self.value = self.romano_a_entero('XXIV')      Se asigna a self.value el valor de XXIV
            if self.value == 'Error en formato':
                self.rvalue = self.value
            else:
                self.rvalue = valor            #self.rvalue = 'XXIV'                           Se asigna la representación gráfica de XXIV
        else:
            self.value = valor
            self.rvalue = self.entero_a_romano()
            if self.rvalue == 'Overflow':
                self.value = self.rvalue
            
    def romano_a_entero(self, numero_romano):  #colocamos el self al pasar a clase (objeto)
                            #Al incluir la instancia self value, eliminamos el valor numero_romano
        if numero_romano == '':
            return 'Error en formato'
        
        #if len(numero_romanos) > 3:   #Solución pasajera, porque si no me da error cualquier numero mayor de 3 dígitos que meta
        # return 'Error en formato'

        entero = 0
        numRepes = 0
        letraAnt = ''
        #La última operación fue una resta
        fueResta = False  #Es una solución al hecho de que no se pueden tener dos restas seguidas, como es el caso de IXL
        for letra in numero_romano:  #Recorre cada letra del valor/clave introducido
            
            if letra in self.__symbols:  #Si cada letra de la clave que me has introducido están en el diccionario
                if letraAnt == '' or self.__symbols[letraAnt] >= self.__symbols[letra]:
                    entero += self.__symbols[letra]
                    fueResta = False 
                else:
                    if letraAnt + letra in self.__symbols.keys() and numRepes < 2 and not fueResta:
                        entero = entero - self.__symbols[letraAnt] * 2 + self.__symbols[letra]
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

    def entero_a_romano(self):
        if self.value > 3999 or self.value < 1:
            return 'Overflow'  #Con esta orden validamos la línea 79 del test para que no de error

        componentes = self.__descomponer(self.value)

        res = ''
        for valor in componentes:
            while valor > 0:
                k, v = self.__busca_valor_menor_o_igual(valor)
                valor -= v
                res += k

        return res

    def __busca_valor_menor_o_igual(self, v):  #Al convertir a objeto, hago privado el atributo busca.. (__)
        for key, value in self.__symbols.items():
            if value <= v:
                return key, value

    def __descomponer(self, numero):  #Al convertir a objeto, hago privado el atributo descomponer (__)
    
        res = []
        for orden in range(3, 0, -1):
            resto = numero % 10 ** orden
            res.append(numero - resto)
            numero = resto
        res.append(numero)
        return res

    def __str__(self):
        return self.rvalue

    def __repr__(self):
        return self.rvalue 

    def __add__(self, other):   #Método mágico (value es un nombre que asignamos nosotros a voluntad)
        #        I,     III
        if isinstance(other, int):
            suma = self.value + other
        else:
            suma = self.value + other.value 
        resultado = RomanNumber(suma)
        return resultado

    def __radd__(self, other):
        return self.__add__(other) #Para no repetir todo el código de __add__ hacemos un return a la instancia
        '''         #dont repeat yourself
        if isinstance(value, int):
            suma = self.value + value
        else:
            suma = self.value + value.value 
        resultado = RomanNumber(suma)
        return resultado
        '''
    def __sub__(self, other):   # Métodos mágicos
        if isinstance(other, int):
            suma = self.value - other
        else:
            resta = self.value - other.value
        resultado = RomanNumber(resta)
        return resultado

    def __rsub__(self, other):
        return self.__sub__(other)

    def __eq__(self, other):
        return self.value == other.value