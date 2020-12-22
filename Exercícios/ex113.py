# Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de número de
# tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade


def leiaInt(txt):
    while True:
        try:
            n = int(input(txt))
        except (ValueError, TypeError):
            print(f'\033[31mERRO! DIGITE UM VALOR INTEIRO\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[33mEntrada de dados interrompida pelo usuário\033[m')
            return 0
        else:
            return n


def leiaFloat(txt):
    while True:
        try:
            n = float(input(txt))
        except (ValueError, TypeError):
            print('\033[31mERRO! DIGITE UM VALOR REAL\033[m')
        except (KeyboardInterrupt):
            print('\n\033[33mEntrada de dados interrompida pelo usuário\033[m')
            return 0
        else:
            return n


i = leiaInt('Digite um valor inteiro: ')
r = leiaFloat('Digite um valor real: ')
print(f'Você digitou {i} como inteiro e {r} como real')
