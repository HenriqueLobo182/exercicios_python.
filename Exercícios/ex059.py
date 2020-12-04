# Crie um programa que leia dois valores e mostre um menu na tela:
# [1] somar.
# [2] multiplicar.
# [3] maior.
# [4] novos números.
# [5] sair do programa.
# Seu programa deverá realizar a operação solicitada em cada caso.

from time import sleep

v1 = int(input('Digite um valor: '))  # primeiro valor
v2 = int(input('Digite outro valor: '))  # segundo valor
a = 0  # ação do usuário
while a != 5:
    a = int(input("""[1] somar 
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa
O que deseja fazer com os valores {} e {}? """.format(v1, v2)))
    if a == 1:
        print('{} + {} = {}'.format(v1, v2, (v1+v2)))
    elif a == 2:
        print('{} x {} = {}'.format(v1, v2, (v1*v2)))
    elif a == 3:
        if v1 > v2:
            print('{} > {}'.format(v1, v2))
        elif v1 == v2:
            print('{} = {}'.format(v1, v2))
        else:
            print('{} < {}'.format(v1, v2))
    elif a == 4:
        v1 = int(input('Digite um valor: '))
        v2 = int(input('Digite outro valor: '))
    elif a == 5:
        print('Saindo do programa...')
        sleep(2)
    else:
        print('Ação desconhecida. Tente novamente!')
        sleep(2)
    print('=-'*20)
print('FIM')
