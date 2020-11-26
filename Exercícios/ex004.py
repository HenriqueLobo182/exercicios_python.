# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as
# informações possíveis sobre ele.

n = input('Digite algo: ')
print('{} O tipo primitivo desse valor é'.format(n), type(n))
print('{} So tem espaços?'.format(n), n.isspace())
print('{} É um número?'.format(n), n.isnumeric())
print('{} É alfabético?'.format(n), n.isalpha())
print('{} É alfanumérico?'.format(n), n.isalnum())
print('{} Está todo maiúsculo?'.format(n), n.isupper())
print('{} Está todo minúsculo?'.format(n), n.islower())
print('{} É capitalizada?'.format(n), n.istitle())
