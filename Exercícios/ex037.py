# Escreva um programa que leia um número Inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 para binário.
# 2 para octal.
# 3 para hexadecimal.

n = int(input('Digite um número: '))

print('==-'*15)
print('[1] para binário.')
print('[2] para octal')
print('[3] para hexadecimal')
ec = int(input('Escolha a conversão: '))  # escolha usuário

if ec == 1:
    print('O número {} em binário corresponde a {}'.format(n, bin(n)[2:]))
elif ec == 2:
    print('O número {} em octal corresponde a {}'.format(n, oct(n)[2:]))
elif ec == 3:
    print('O número {} em hexadecimal corresponde a {}'.format(n, hex(n)[2:]))
else:
    print('Escolha uma conversão válida!')
