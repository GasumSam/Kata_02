def doble(x):
    return x * 2

class Persona():

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __repr__(yomismo):
        return 'Me llamo {} y tengo {} alo/s' .format(yomismo.name, yomismo.age)

    def dimequieeres(cosita):
        return cosita.__repr__()luis

luis = Persona('Luis', 19) #Instancia a la clase
mon = Persona('Ramón', 50)

print(luis.dimequieeres())
#print(cosita) #No va a funcionar porque la función cosita solo va a funcionar en las líneas 13 y 14 (función) #Es el ámbito en el que funciona la variable

#print(doble(luis.self.edad)) #No funciona porque self no existe, solo vale para la definición dentro de la función