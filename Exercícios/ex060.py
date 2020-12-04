# Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Exemplo: 5! = 5x4x3x2x1 = 120

from math import factorial
n = int(input('Digite um número e calcule sua fatorial: '))  # número digitado
c = n  # número original digitado
print('{}!'.format(n), end=' = ')
while c != 0:
    if c > 1:
        print('{}'.format(c), end=' x ')
    else:
        print('{}'.format(c), end=' = ')
    c -= 1
print('{}'.format(factorial(n)))
