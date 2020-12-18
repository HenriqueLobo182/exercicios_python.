# Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai
# aparecer. Quando o usuário digitar a palavra "FIM", o programa se encerrará
# Observação: use cores

from time import sleep

cor = {'verde': '\033[42m', 'branco': '\033[7m', 'azul': '\033[44m', 'vermelho': '\033[41m'}


def ajuda(txt):
    titulo(f'Acessando {txt}', cor['azul'])
    print(f'{cor["branco"]}', end='')
    help(txt)
    print('\033[m', end='')
    sleep(1)


def titulo(msg, cor="\033[m"):
    tamanho = len(msg) + 6
    print(cor, end='')
    print(f'~'*tamanho)
    print(f'   {msg}')
    print(f'~'*tamanho)
    print("\033[m", end='')
    sleep(1)


msg = ' '
while True:
    titulo('CENTRAL DE AJUDA PYTHON', cor['verde'])
    msg = str(input('Função ou biblioteca: '))

    if msg.upper() == 'FIM':
        break
    else:
        ajuda(msg)
titulo('PROGRAMA ENCERRADO', cor['vermelho'])
