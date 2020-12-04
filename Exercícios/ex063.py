# Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma Sequência
# de Fibonacci.
# 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8

print('='*30)
print('SEQUÊNCIA DE FIBONACCI')
print('='*30)
termos = int(input('Você quer ver quantos termos? '))
c = 0
f = 0
f1 = 1
f2 = 0
while c != termos:
    print('{} -> '.format(f), end='')
    f = f1 + f2
    f2 = f1
    f1 = f
    f = f2
    c += 1
print('FIM')

print('=-'*40)  # OU

n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('{} -> {}'.format(t1, t2), end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(' -> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' -> FIM')
