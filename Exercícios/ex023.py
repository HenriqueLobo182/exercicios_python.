# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados
# Exemplo: 1834
# Unidade: 4
# Dezena: 3
# Centena: 8
# Milhar: 1

numero = int(input('Digite um número: '))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print('Analisando o número {}'.format(numero))
print('Unidade {}'.format(u))
print('Dezena {}'.format(d))
print('Centena {}'.format(c))
print('Milhar {}'.format(m))
