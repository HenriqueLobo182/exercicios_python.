# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar
# descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep

print('==-'*12)
print('Vou pensar em um número de 0 a 5')
print('==-'*12)
sleep(1)

nc = randint(0, 5)  # número escolhido pelo computador
nu = int(input('Em que número pensei? '))  # número escolhido pelo usuário

print('PROCESSANDO...')
sleep(1)
if nc == nu:
    print('Parabéns você adivinhou o número!')
else:
    print('Eu escolhi o número {} e não o número {}. Tente novamente!'.format(nc, nu))
