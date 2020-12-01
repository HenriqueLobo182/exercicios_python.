# Crie um programa que leia um número Inteiro qualquer e mostre na tela se ele é PAR ou ÍMPAR.

n = int(input('Digite um número Inteiro: '))
if (n % 2) == 0:
    print('O número {} é par'.format(n))
else:
    print('O número {} é ímpar'.format(n))
