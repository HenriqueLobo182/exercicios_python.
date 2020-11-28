# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira
# Exemplo: 6.127 tem como porção inteira 6

from math import trunc
numero = float(input('Digite um número: '))
print('A porção inteira de {} vale {}'.format(numero, int(numero)))

print('==-'*15)  # ou

print('A porção inteira de {} vale {}'.format(numero, trunc(numero)))
