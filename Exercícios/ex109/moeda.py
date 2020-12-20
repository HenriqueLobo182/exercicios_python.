def metade(n=0, sit=False):
    resultado = n / 2
    if sit:
        return moeda(resultado)
    else:
        return resultado


def dobro(n=0, sit=False):
    resultado = n * 2
    if sit:
        return moeda(resultado)
    else:
        return resultado


def aumentar(n=0, porc=0, sit=False):
    """
    -> Calcula o aumento percentual de n
    :param n: valor a ser formatado
    :param porc: porcentagem para aumento
    :param sit: com ou sem "R$"
    :return: retorno o valor reajustado
    """
    resultado = n + (n * porc/100)
    if sit:
        return moeda(resultado)
    else:
        return resultado


def diminuir(n=0, porc=0, sit=False):
    resultado = n - (n * porc/100)
    if sit:
        return moeda(resultado)
    else:
        return resultado
    # return resultado if sit is False else moeda(resultado)

def moeda(v=0, moeda='R$'):
    return f'{moeda}{v:>.2f}'.replace('.', ',')
