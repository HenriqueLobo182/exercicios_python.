# Faça um programa que tenha uma função chamada contador(), que recebe três parâmetros: início, fim e passo e realize a
# contagem.
# Seu programa tem que realizar três contagens através da função criada:
# a) De 1 até 10, de 1 em 1.
# b) de 10 até 0, de 2 em 2.
# c) Uma contagem personalizada.

from time import sleep


def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1

    if i < f:
        print(f'Sequência {i} até {f} pulando de {p} em {p}:')
        for c in range(i, f+1, p):
            print(f'{c} ', end='')
            sleep(1)

    else:
        print(f'Sequência {i} até {f} pulando de {p} em {p}:')
        for c in range(-i, -f+p, p):
            print(f'{-c} ', end='')
            sleep(1)
    print('FIM!')
    print('~' * 50)


contador(1, 10, 1)
contador(10, 0, -2)
contador(i=int(input('Início: ')),
         f=int(input('Fim: ')),
         p=int(input('Passo: ')))


# OU


def contadorr(ii, ff, pp):
    if pp < 0:
        pp *= -1

    if pp == 0:
        pp += 1

    print(f'Contagem de {ii} até {ff} de {pp} em {pp}')

    if ii < ff:
        cont = ii
        while cont <= ff:
            print(f'{cont} ', end='', flush=True)
            sleep(1)
            cont += pp
        print(f'FIM')
    else:
        cont = ii
        while cont >= ff:
            print(f'{cont} ', end='', flush=True)
            sleep(1)
            cont -= pp
        print('FIM')


contadorr(1, 10, 1)
contadorr(10, 0, 2)
print('~'*40)
print('Agora é sua vez de escolher!')
ini = int(input('Início: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)
