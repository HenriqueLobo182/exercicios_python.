# Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão
# gerados e cai sortear 6 números entre 1 e 60 para jogo, cadastrando tudo em uma lista composta.

from random import choice
from time import sleep

print('=-'*20)
print('{:^40}'.format('PALPITES DA MEGA SENA'))
print('=-'*20)

numeros = list()
for n in range(1, 61):  # gerando 60 números
    numeros.append(n)

jogo = []
jogos = int(input('Deseja sortear quantos jogos? '))
for cont in range(1, (jogos + 1)):
    print(f'{cont}º jogo:', end='')
    for j in range(0, 6):
        escolha = choice(numeros)
        jogo.append(escolha)
        numeros.remove(escolha)
    jogo.sort()
    print(f'{jogo}', end='')
    jogo.clear()
    print()
    sleep(1)
print('=-'*20)
print(f'{"BOA SORTE!!!":^40}')


print('=-'*20)  # OU


from random import randint
jogos = list()
lista = list()
tot = 1
quant = int(input('Quantos jogos você quer? '))
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('=-'*3, f'SORTEANDO {quant} JOGOS', '=-'*3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('=-'*5, 'BOA SORTE', '=-'*5)
