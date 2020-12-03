# Faça um programa que leia um número inteiro e diga se ele é ou não número primo.

cores = {'vermelho': '\033[31m', 'verde': '\033[32m', 'limpa': '\033[m'}

n = int(input('Digite um número: '))
print('=-'*20)

cont = 0
cont2 = 0
for c in range(1, n+1):
    if n % c == 0:
        cont += 1
if cont != 2:
    print('{}NÃO É PRIMO{}'.format(cores['vermelho'], cores['limpa']))
else:
    print('{}É PRIMO{}'.format(cores['verde'], cores['limpa']))
print('{} números dividiram {} e tiveram resto 0'.format(cont, n))

print('=-'*20)  # OU

num = int(input('Digite um número: '))
total = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[32m', end='')
        total += 1
    else:
        print('\033[31m', end='')
    print('{}'.format(c), end=' ')
print('\n\033[mO número {} foi divisível {} vezes'.format(num, total))
if total == 2:
    print('PRIMO')
else:
    print('NÃo É PRIMO')
