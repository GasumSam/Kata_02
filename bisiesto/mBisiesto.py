def esBisiesto(anno):
    return anno % 4 == 0 or (anno % 400 == 0 and anno % 100 != 0)

def esEntero(n):
    try:
        n = int(n)
        return True
    except ValueError:
        return False