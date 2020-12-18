# Crie um programa que tenha a função leiaint(), que vai funcionar de forma semelhante à função input() do Python, só
# que fazendo a validação para aceitar apenas um valor numérico
# Exemplo: n = leiaint('Digite um n')

cor = {'vermelho': '\033[31m', 'limpa': '\033[m'}


def leiaInt(txt):
    while True:
        n = str(input(txt))
        if n.isnumeric():
            txt = int(n)
            break
        else:
            print(f'{cor["vermelho"]}ERRO! DIGITE UM VALOR INTEIRO{cor["limpa"]}')
    return txt


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
