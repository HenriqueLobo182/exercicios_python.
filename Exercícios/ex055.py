# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

import math
maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Peso da {}ª pessoa em kg: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso informado foi de {}kg'.format(maior))
print('O menor peso informado foi de {}kg'.format(menor))
