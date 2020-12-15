# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteio() e somaPar(). A primeira função
# Vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores
# pares sorteados pela função anterior.

from random import randint
from time import sleep
numeros = []
print(f'Sorteando os 5 números da lista, temos: ', end='')


def sorteio(*s):
    for v in s:
        print(f'{v} ', end='')
        numeros.append(v)
        sleep(0.3)


for cont in range(0, 5):
    sorteio(randint(1, 10))
print('PRONTO')


def somapar(n):
    soma = 0
    for v in n:
        if v % 2 == 0:
            soma += v
    print(f'Somando os pares de {n} temos {soma}')


somapar(numeros)
