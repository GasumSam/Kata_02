
def esbisiesto(anno):
    return anno % 4 == 0 or (anno % 400 == 0 and anno % 100 != 0):

n = input('Año: ')

while no esbisiesto(int(n))if __name__ == "__main__":
    print(n, 'no es bisiesto. Vuelve a probar')
    n = input('Año: ')

print('Este sí ', n , 'es bisiesto')

'''


if esbisiesto(n):
    print(n, 'es bisiesto')
else:
    print(n, 'no es bisiesto')



def esBisiesto(anno):
    if anno % 4 != 0 or (anno % 100 == 0 and anno % 400 != 0):
        #print('El año' anno 'no es bisiesto')
        return True
    else:
        return False
        #print('El año' anno 'es bisiesto')

def esBisiesto(n):
    if n % 400 == 0 or (n % 4 == 0 and n % 100 % 0):
        return True
    else:
        return False


n = input('Año')
n = int(n)
print(esBisiesto(n))
'''
