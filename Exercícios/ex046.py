# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0,
# com uma pausa de 1 segundo entre eles.

from emoji import emojize
from time import sleep
cores = {'verde': '\033[1:32m', 'limpa': '\033[m'}

for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('{} {} {} {}BOOM{} {} {} {}'.format(emojize(':boom:', use_aliases=True), emojize(':boom:', use_aliases=True),
                                          emojize(':boom:', use_aliases=True), cores['verde'], cores['limpa'],
                                          emojize(':boom:', use_aliases=True), emojize(':boom:', use_aliases=True),
                                          emojize(':boom:', use_aliases=True)))
