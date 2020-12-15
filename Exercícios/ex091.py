# Crie um programa onde 4 jogadores joguem um dado e tenhas resultados aleatórios. Guarde esses resultados em um
# dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep

jogo = dict()

jogo['Jogador1'] = randint(1, 6)
jogo['Jogador2'] = randint(1, 6)
jogo['Jogador3'] = randint(1, 6)
jogo['Jogador4'] = randint(1, 6)
jogoordem = jogo.copy()  # recebe uma cópia da lista principal
jogoordem = sorted(jogoordem.values(), reverse=True)  # ordem decrescente do sorteio do dado

print('Valores sorteados: ')
for k, v in jogo.items():
    print(f' - {k} tirou {v} no dado')
    sleep(1)

print('~'*50)
sleep(1)
print('  == RANKING DOS JOGADORES ==')
sleep(1)

for cont in range(0, 4):
    for k, v in jogo.items():
        if jogoordem[cont] == v:
            print(f'{cont + 1}º Lugar: {k} que tirou {v}')
            jogo.pop(k)
            sleep(1)
            break


print('=-'*30)  # OU


from operator import itemgetter

jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}

ranking = list()
print('Valores sorteados:')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('~'*40)
print('== RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}')
