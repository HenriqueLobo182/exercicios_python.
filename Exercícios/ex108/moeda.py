def metade(n=0):
    resultado = n / 2
    return resultado


def dobro(n=0):
    resultado = n * 2
    return resultado


def aumentar(n=0, porc=0):
    resultado = n + (n * porc/100)
    return resultado


def diminuir(n=0, porc=0):
    resultado = n - (n * porc/100)
    return resultado


def moeda(n=0, moeda='R$'):
    return f'{moeda}{n:>.2f}'.replace('.', ',')
