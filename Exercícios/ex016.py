# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira
# Exemplo: 6.127 tem como porção inteira 6

from math import trunc
number = float(input('Type a number: '))
print(f'The non-decimal portion of {number} is worth {int(number)}')
print('==-'*15)  # or
print(f'The non-decimal portion of {number} is worth {trunc(number)}')
