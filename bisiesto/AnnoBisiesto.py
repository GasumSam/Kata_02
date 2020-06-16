def Negativo(numero):
    if int(numero)<1:
        return True
    else:
        return False

def exception(anno):
    try:
        int(anno)
        return True
    except:
        print('Ocurrió un error')
        return False

def Bisiesto(anno):
    num = int(anno)
    if num % 4 == 0 and num % 100 != 0 or num % 400 == 0:
        return True
    else:
        return False
        