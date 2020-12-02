# Crie um programa que faça o computador jogar Jokenpô com você.

from emoji import emojize
from random import randint
from time import sleep

cores = {'vermelho': '\033[31m', 'verde': '\033[32m', 'amarelo': '\033[33m', 'limpa': '\033[m'}

print('=-'*11)
print('Vamos jogar Jokenpô?')
print('=-'*11)
sleep(1)

print("""[0] PEDRA 
[1] PAPEL 
[2] TESOURA""")

jogo = ('PEDRA', 'PAPEL', 'TESOURA')
ec = randint(0, 2)  # escolha do computador
eu = int(input('Sua escolha: '))  # escolha do usuário

if eu != 0 and eu != 1 and eu != 2:
    print('{} {}Tente novamente{} {}'.format(emojize(":warning:", use_aliases=True), cores['vermelho'],
                                             cores['limpa'], emojize(":warning:", use_aliases=True)))
else:
    print("""Computador: {}
Usuário: {}""".format(jogo[ec], jogo[eu]))

if ec == 0:
    if eu == 0:
        print('{} {}Empate{} {}'.format(emojize(":punch:", use_aliases=True), cores['amarelo'], cores['limpa'],
                                        emojize(":punch:", use_aliases=True)))
    elif eu == 1:
        print('{} {}Você ganhou{} {}'.format(emojize(":punch:", use_aliases=True), cores['verde'], cores['limpa'],
                                             emojize(":hand:", use_aliases=True)))
    elif eu == 2:
        print('{} {}Você perdeu{} {}'.format(emojize(":punch:", use_aliases=True), cores['vermelho'], cores['limpa'],
                                             emojize(":v:", use_aliases=True)))
    else:
        print('{} {}Jogada inválida{} {}'.format(emojize(":warning:", use_aliases=True), cores['vermelho'],
                                                 cores['limpa'], emojize(":warning:", use_aliases=True)))

elif ec == 1:
    if eu == 0:
        print('{} {}Você perdeu{} {}'.format(emojize(":hand:", use_aliases=True), cores['vermelho'], cores['limpa'],
                                             emojize(":punch:", use_aliases=True)))
    elif eu == 1:
        print('{} {}Empate{} {}'.format(emojize(":hand:", use_aliases=True), cores['amarelo'], cores['limpa'],
                                        emojize(":hand:", use_aliases=True)))
    elif eu == 2:
        print('{} {}Você ganhou{} {}'.format(emojize(":hand:", use_aliases=True), cores['verde'], cores['limpa'],
                                             emojize(":v:", use_aliases=True)))
    else:
        print('{} {}Jogada inválida{} {}'.format(emojize(":warning:", use_aliases=True), cores['vermelho'],
                                                 cores['limpa'], emojize(":warning:", use_aliases=True)))

elif ec == 2:
    if eu == 0:
        print('{} {}Você ganhou{} {}'.format(emojize(":v:", use_aliases=True), cores['verde'], cores['limpa'],
                                             emojize(":punch:", use_aliases=True)))
    elif eu == 1:
        print('{} {}Você perdeu{} {}'.format(emojize(":v:", use_aliases=True), cores['vermelho'], cores['limpa'],
                                             emojize(":hand:", use_aliases=True)))
    elif eu == 2:
        print('{} {}Empate{} {}'.format(emojize(":v:", use_aliases=True), cores['amarelo'], cores['limpa'],
                                        emojize(":v:", use_aliases=True)))
    else:
        print('{} {}Jogada inválida{} {}'.format(emojize(":warning:", use_aliases=True), cores['vermelho'],
                                                 cores['limpa'], emojize(":warning:", use_aliases=True)))
