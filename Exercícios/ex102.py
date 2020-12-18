# Crie um programa que tenha uma função() que receba dois parâmetros: o primeiro que indique o número a calcular e o
# outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de
# cálculo do fatorial.

from math import factorial


def função(n=1, show=False):
    """
    -> Fatorial de um número n qualquer
    :param n: número escolhido
    :param show: (opcional) mostra ou não a multiplicação
    :return: sem return
    """
    fatorial = factorial(n)
    print(f'{n}! = ', end='')
    if show is True:
        for c in range(n, 0, -1):
            if c == 1:
                print(f'{c} = {fatorial}')
            else:
                print(f'{c} x ', end='')
    else:
        print(f'{fatorial}')


função(5, True)
help(função)


print('~'*60)  # OU


def fatorial(nn, show=False):
    f = 1
    for c in range(nn, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


print(fatorial(5, show=True))
