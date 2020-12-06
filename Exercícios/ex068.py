# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint
c = 0  # contador de vitórias do usuário

print('=-'*10)
print('PAR OU ÍMPAR')
print('=-'*10)

while True:
    eu = int(input('Escolha um número: '))  # primeira escolha do usuário
    ec = randint(0, 10)  # sorteio do computador
    soma = eu + ec
    eu2 = ' '
    while eu2 not in 'PpÍI':
        eu2 = str(input('Escolha entre PAR ou ÍMPAR: ')).strip().upper()[0]  # segunda escolha do usuário
    if soma % 2 == 0:
        if eu2 in 'Pp':
            print(f'Usuário escolheu {eu} e PAR')
            print(f'Computador escolheu {ec} e ÍMPAR')
            print(f'{eu} + {ec} = {soma}, portanto, PAR')
            print('Usuário venceu!')
        elif eu2 in 'ÍI':
            print(f'Usuário escolheu {eu} e ÍMPAR')
            print(f'Computador escolheu {ec} e PAR')
            print(f'{eu} + {ec} = {soma}, portanto, PAR')
            print('Computador venceu!')
            break
    elif soma % 2 != 0:
        if eu2 in 'ÍI':
            print(f'Usuário escolheu {eu} e ÍMPAR')
            print(f'Computador escolheu {ec} e PAR')
            print(f'{eu} + {ec} = {soma}, portanto, ÍMPAR')
            print('Usuário venceu!')
        elif eu2 in 'Pp':
            print(f'Usuário escolheu {eu} e PAR')
            print(f'Computador escolheu {ec} e ÍMPAR')
            print(f'{eu} + {ec} = {soma}, portanto, ÍMPAR')
            print('Computador venceu')
            break
    print('='*35)
    c += 1

print('~'*40)
print(f'Terminou com {c} vitórias consecutivas')
