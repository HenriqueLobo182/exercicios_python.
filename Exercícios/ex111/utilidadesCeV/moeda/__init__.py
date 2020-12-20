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
    resultado = n + (n * porc / 100)
    if sit:
        return moeda(resultado)
    else:
        return resultado


def diminuir(n=0, porc=0, sit=False):
    resultado = n - (n * porc / 100)
    if sit:
        return moeda(resultado)
    else:
        return resultado
    # return resultado if sit is False else moeda(resultado)


def moeda(v=0, moeda='R$'):
    return f'{moeda}{v:>.2f}'.replace('.', ',')


def resumo(n=0, taxaau=0, taxadi=0):
    """
    -> Função que reduz a quantidade de prints no programa principal
    :param n: valor a ser formatado
    :param taxaau: taxa para aumentar uma porcentagem de n
    :param taxadi: taxa para diminuir uma porcentagem de n
    :return: sem retorno
    """
    print('~'*30)
    print(f"Analisando {moeda(n)}".center(30))
    print('~'*30)
    print(f'{"Metade:":.<21}{metade(n, True)}')
    print(f'{"Dobro:":.<21}{dobro(n, True)}')
    print(f'Aumentando {taxaau}{"%":.<8}{aumentar(n, taxaau, True)}')
    print(f'Reduzindo {taxadi}{"%":.<9}{diminuir(n, taxadi, True)}')
    print('~'*30)
