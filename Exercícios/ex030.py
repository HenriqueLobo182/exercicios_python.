# Crie um programa que leia um número Inteiro qualquer e mostre na tela se ele é PAR ou ÍMPAR.

number = int(input('Type a integer: '))
if (number % 2) == 0:
    print(f'The number {number} is even')
else:
    print(f'The number {number} is odd')
